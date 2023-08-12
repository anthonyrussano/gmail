# Email Search App

This application is designed to connect to an email server, download emails from a specific sender (in this case, "scholaralerts-noreply@google.com"), and store them in a local SQLite database. Through a web interface, users can then search the contents of these emails using specific keywords.

## Features:

1. **Email Downloading**: The app connects to an IMAP email server and fetches emails from a specified sender, storing the email content in a local database.
2. **Keyword Search**: Via the web interface, users can input keywords to search the content of the stored emails. Search results will display the email content in an iframe.
3. **Improved Link Behavior**: Any links within the displayed emails will open in a new browser tab, ensuring users don't navigate away from the search results.

## Prerequisites:

- Python 3
- Flask
- Flask-SQLAlchemy
- IMAP client access enabled for your email account

## Setup:

1. **Environment Variables**:
   - Ensure you have a `.env` file with necessary credentials (or you can use the `vars.py` module).
   - Use the `dotenv` library to load these variables into the environment.

2. **SQLite Database**:
   - The app uses SQLite to store the email data. Ensure you have SQLite installed.
   - The database file (`emails.db`) will be created in the root directory of the project.

3. **Python Libraries**:
   - You need to have Flask, Flask-SQLAlchemy, and other required libraries installed. You can typically install these with `pip`.

```bash
pip install Flask Flask-SQLAlchemy python-dotenv
```

## Usage:

1. **Start the App**:
   - Navigate to the project directory and run the script. This will start the Flask server.
   
```bash
python your_script_name.py
```

2. **Download Emails**:
   - Once the server is running, navigate to `http://localhost:5000/download_emails` in your web browser. This will trigger the email downloading process.

3. **Search Emails**:
   - Go to the home page at `http://localhost:5000/`.
   - Enter your search keywords and hit "Search". The emails containing those keywords will be displayed below.

## Note:

The application is designed for demonstration purposes and uses a delay of 0.1 seconds between downloading individual emails to avoid potential rate limits or rapid consecutive requests to the email server. Adjust as necessary for your use case.

---

This README provides a comprehensive overview of the application, its features, setup, and usage. You can expand on this by adding sections about deployment, contributions, or any other relevant details you'd like to share.
