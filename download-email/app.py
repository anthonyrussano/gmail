import imaplib
import email
import os
from vars import EMAIL, PASSWORD, MAIL_SERVER 
def fetch_and_save_emails(email_ids):
    for email_id in email_ids:
        status, data = mail.fetch(email_id, '(RFC822)')
        
        # Parse the email content
        msg = email.message_from_bytes(data[0][1])
        email_subject = msg['subject']
        email_date = msg['date']
        email_body = ""
        # Check if the email is multipart (e.g., both text and HTML parts)
        if msg.is_multipart():
            # Iterate through each part of the email
            for part in msg.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))

                # If the email part is text/html and not an attachment, get its content
                if content_type == "text/html" and "attachment" not in content_disposition:
                    email_body = part.get_payload(decode=True).decode('utf-8', errors='replace')
                    break
        else:
            # If email is not multipart, just get its payload
            email_body = msg.get_payload(decode=True).decode('utf-8', errors='replace')

        # Save the email content to an .html file
        filename = os.path.join(SAVE_DIRECTORY, f"email_{email_id.decode('utf-8')}.html")
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(email_body)
        
        print(f"Saved email {email_id.decode('utf-8')} to {filename}")


EMAIL = EMAIL
PASSWORD = PASSWORD
MAIL_SERVER = MAIL_SERVER
SAVE_DIRECTORY = 'saved_emails'  # Directory where emails will be saved

# Connect to the mail server and select the mailbox
mail = imaplib.IMAP4_SSL(MAIL_SERVER)
mail.login(EMAIL, PASSWORD)
mail.select('inbox')

# Ensure the save directory exists
if not os.path.exists(SAVE_DIRECTORY):
    os.makedirs(SAVE_DIRECTORY)

# Search for emails from scholaralerts-noreply@google.com
status, email_ids = mail.search(None, '(FROM "scholaralerts-noreply@google.com")')
num_emails = len(email_ids[0].split())

if num_emails:
    print(f"Found {num_emails} emails from scholaralerts-noreply@google.com.")
    user_input = input("Do you want to download and save these emails? (yes/no): ").strip().lower()

    if user_input == 'yes':
        fetch_and_save_emails(email_ids[0].split())
    else:
        print("Emails were not saved.")

else:
    print(f"No emails from scholaralerts-noreply@google.com found.")

# Close the mailbox and logout from the server
mail.close()
mail.logout()
