# 📧 Bulk Email Sender

A Streamlit-based web application that allows users to send emails to multiple recipients with attachments using Gmail.

## Features

- Send emails to multiple recipients
- Support for file attachments
- Secure authentication using Gmail App Passwords
- Multiple recipient support with comma-separated emails
- Preserves original file names and formats for attachments
- Clean and intuitive user interface
- Fast and efficient email sending

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

```
bulk-email-sender/
├── .venv/                  # Virtual environment
├── .idea/                  # IDE configuration files
├── app.py                  # Core email sending functionality
├── main.py                 # Streamlit application entry point
├── requirements.txt        # Project dependencies
└── README.md              # Project documentation
```

## Troubleshooting

### Common Issues

1. **"Command not found" errors**
   - Make sure your virtual environment is activated
   - Verify that all dependencies are installed correctly

2. **Gmail Authentication Errors**
   - Ensure 2-Step Verification is enabled
   - Verify that you're using an App Password, not your regular Gmail password
   - Check if your Gmail account has less secure app access enabled

3. **File Attachment Issues**
   - Check file size limits (Gmail has a 25MB limit per email)
   - Ensure file permissions are correct
   - Verify file path is accessible

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Email functionality powered by Python's `smtplib`
- Icons provided by [Emoji](https://emojipedia.org/)

## Support

If you encounter any issues or have questions, please open an issue in the GitHub repository.
