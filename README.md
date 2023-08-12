# Gmail Processing Repo

This repo contains two apps designed to process and interact with emails from "scholaralerts-noreply@google.com". One application is a Flask-based web interface that allows users to search through the content of these emails. The other is a standalone script that downloads the emails and saves them as individual HTML files.

## Applications:

1. **Email Search App (Flask)**:
    - A Flask application that connects to an IMAP email server, fetches emails from the specified sender, and stores them in a SQLite database.
    - Offers a web-based interface for users to search the email content using keywords.
    
2. **Email Downloader**:
    - A standalone Python script that connects to an IMAP email server and searches for emails from the specified sender.
    - Saves the content of these emails as individual HTML files in a local directory.

## Prerequisites:

- Python 3
- Flask
- Flask-SQLAlchemy
- IMAP client access enabled for your email account
- These scripts rely on using an app password to access your gmail account.
  - An app password is a 16-character code that you can generate to let you sign into your Google Account from apps, without using 2FA.
  - To create an app password, you need 2-Step Verification enabled on your Google Account.
  - Go to your Google Account (https://myaccount.google.com/).
  - Select Security.
  - Under "Signing in to Google," select 2-Step Verification.
  - At the bottom of the page, select App passwords.
  - Enter a name that helps you remember where you’ll use the app password.
  - Select Generate.
  - Copy the password (store securely as you would other secrets).
  - Select Done. 

## Notes:

- The applications are designed for demonstration and learning purposes.
