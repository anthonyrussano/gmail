import os
import time
import imaplib
import email
from email.header import decode_header
from flask import Flask, render_template_string, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_  # <-- Add this line
from dotenv import load_dotenv
from vars import EMAIL, PASSWORD, IMAP_SERVER 

# Load environment variables
load_dotenv()

# Email Configuration
IMAP_SERVER = IMAP_SERVER
IMAP_PORT = 993  # This is typically the port for IMAP over SSL
EMAIL = EMAIL
PASSWORD = PASSWORD

# Connects to the email server and logs in
def connect_to_email():
    mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
    mail.login(EMAIL, PASSWORD)
    return mail

# Fetch emails from a particular sender
def fetch_emails_from_sender(mail, sender_email):
    mail.select('inbox')
    status, messages = mail.search(None, '(FROM "{}")'.format(sender_email))
    email_ids = messages[0].split()
    return email_ids

# Get the email content
def get_email_content(mail, email_id):
    status, msg_data = mail.fetch(email_id, '(RFC822)')
    for response_part in msg_data:
        if isinstance(response_part, tuple):
            msg = email.message_from_bytes(response_part[1])
            subject = decode_header(msg["Subject"])[0][0]
            if isinstance(subject, bytes):
                subject = subject.decode()
            if msg.is_multipart():
                for part in msg.walk():
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    if "attachment" not in content_disposition:
                        body = part.get_payload(decode=True).decode()
                        return subject, body
            else:
                body = msg.get_payload(decode=True).decode()
                return subject, body
    return None, None

# Flask App
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emails.db'
db = SQLAlchemy(app)

# Define the Email model
class Email(db.Model):
    id = db.Column(db.String, primary_key=True)  # Email's unique ID
    subject = db.Column(db.String, nullable=False)
    body = db.Column(db.Text, nullable=False)

@app.route('/download_emails', methods=['GET'])
def download_emails():
    mail = connect_to_email()
    email_ids = fetch_emails_from_sender(mail, 'scholaralerts-noreply@google.com')
    for email_id in email_ids:
        email_id_str = email_id.decode()
        if not db.session.query(Email).get(email_id_str):
            subject, body = get_email_content(mail, email_id)
            new_email = Email(id=email_id_str, subject=subject, body=body)
            db.session.add(new_email)
            db.session.commit()
            time.sleep(0.1)  # add a delay
    return "Emails downloaded!"

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    keyword_input = request.form.get('keyword')
    if keyword_input:
        keywords = keyword_input.split()  # Split by spaces to get a list of keywords
        filter_conditions = [Email.body.contains(keyword) for keyword in keywords]
        results = Email.query.filter(and_(*filter_conditions)).all()
    return render_template_string("""
        <script>
            function openLinksInNewTab(iframeElement) {
                var iframeContent = iframeElement.contentWindow.document;
                var links = iframeContent.querySelectorAll('a');
                links.forEach(function(link) {
                    link.setAttribute('target', '_blank');
                });
            }
        </script>
        
        <form method="post">
            Keyword: <input type="text" name="keyword">
            <input type="submit" value="Search">
        </form>
        <hr>
        {% for email in results %}
            <div>
                <h3>{{ email.subject }}</h3>
                <iframe srcdoc="{{ email.body }}" width="100%" height="500" onload="openLinksInNewTab(this)"></iframe>
            </div>
            <hr>
        {% endfor %}
    """, results=results)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host="0.0.0.0", port="5000")
