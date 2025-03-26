# 📧 Bulk Email Sender

A Streamlit-based web application that allows users to send emails to multiple recipients with attachments using Gmail.

## Features

- 📨 Send emails to multiple recipients
- 📎 Support for file attachments
- 🔒 Secure authentication using Gmail App Passwords
- 👥 Multiple recipient support with comma-separated emails
- 📁 Preserves original file names and formats for attachments

## Prerequisites

- Python 3.9 or higher
- Gmail account
- Gmail App Password (2FA must be enabled)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/bulk-email-sender.git
cd bulk-email-sender
```

2. Create a virtual environment (recommended):
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the application:
```bash
streamlit run main.py
```

2. Open your web browser and navigate to the provided URL (typically http://localhost:8501)

3. Fill in the required information:
   - Your Gmail address
   - Your Gmail App Password
   - Recipient email addresses (comma-separated)
   - Email subject and body
   - Attach files (optional)

4. Click "Send Email" to send your message

## How to Get Gmail App Password

1. Go to your Google Account settings
2. Navigate to Security
3. Enable 2-Step Verification if not already enabled
4. Go to App Passwords
5. Generate a new app password for "Mail"
6. Use this generated password in the application

## Project Structure 