# Email Downloader

This script is designed to connect to an IMAP email server, specifically search for emails from the sender "scholaralerts-noreply@google.com", and save the content of these emails as HTML files to a local directory.

## Features:

1. **Email Connection**: The script uses the IMAP protocol to connect to an email server and authenticate using the provided credentials.
2. **Email Search**: Once connected, it searches the 'inbox' for emails from "scholaralerts-noreply@google.com".
3. **HTML Email Saving**: Found emails are saved as HTML files in a local directory named `saved_emails`.

## Prerequisites:

- Python 3
- IMAP client access enabled for your email account

## Setup:

1. **Credentials Configuration**:
   - Ensure you have a `vars.py` file that contains your email credentials: `EMAIL`, `PASSWORD`, and `MAIL_SERVER`.
  
2. **IMAP Settings**:
   - Make sure you have IMAP access enabled for your email. This might require you to adjust settings in your email account.

3. **Python Libraries**:
   - This script relies on Python's built-in libraries. No additional installation is required.

## Usage:

1. **Running the Script**:
   - Navigate to the directory containing the script.
   - Run the script using Python:

```bash
python your_script_name.py
```

2. **Email Download**:
   - The script will automatically search for emails from "scholaralerts-noreply@google.com" and will prompt you to confirm if you want to download and save them.
   - If you confirm, the emails will be saved to the `saved_emails` directory as individual HTML files.

## Notes:

- Ensure the email account you're accessing does not have any sensitive information you don't want to download.
- This script saves emails as HTML files, making them viewable in any web browser.
