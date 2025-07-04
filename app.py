import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import mimetypes


def send_email(sender_email, sender_password, to_recipients, cc_recipients=None, bcc_recipients=None, subject="", body="", email_format="plain_text", attachment_path=None):
    smtp_server = "smtp.gmail.com"
    port = 587  # TLS port

    # Create email message
    msg = MIMEMultipart('alternative')
    msg['From'] = sender_email
    msg['To'] = ", ".join(to_recipients)  # Join primary recipients with commas
    msg['Subject'] = subject
    
    # Add CC header if CC recipients are provided
    if cc_recipients:
        msg['Cc'] = ", ".join(cc_recipients)
    
    # Determine the MIME type based on email format
    if email_format == "html":
        # For HTML emails, create both HTML and plain text versions
        # Create a simple plain text version from HTML (basic conversion)
        import re
        plain_text_body = re.sub(r'<[^>]+>', '', body)  # Remove HTML tags
        plain_text_body = re.sub(r'\s+', ' ', plain_text_body)  # Clean up whitespace
        
        # Attach both HTML and plain text versions
        text_part = MIMEText(plain_text_body, 'plain')
        html_part = MIMEText(body, 'html')
        
        msg.attach(text_part)
        msg.attach(html_part)
    else:
        # For plain text emails
        msg.attach(MIMEText(body, 'plain'))

    # Attach file if provided
    if attachment_path:
        try:
            with open(attachment_path, "rb") as attachment:
                # Get the original filename from path
                filename = os.path.basename(attachment_path)
                # Determine the MIME type based on file extension
                content_type, encoding = mimetypes.guess_type(attachment_path)
                if content_type is None:
                    content_type = 'application/octet-stream'

                main_type, sub_type = content_type.split('/', 1)
                part = MIMEBase(main_type, sub_type)
                part.set_payload(attachment.read())

                encoders.encode_base64(part)
                # Ensure filename is properly encoded for email headers
                filename = filename.encode('ascii', 'ignore').decode('ascii')
                part.add_header(
                    'Content-Disposition',
                    'attachment',
                    filename=filename
                )
                msg.attach(part)
        except Exception as e:
            print(f"Error attaching file: {e}")

    # Prepare all recipients for sending (To + CC + BCC)
    all_recipients = to_recipients.copy()
    if cc_recipients:
        all_recipients.extend(cc_recipients)
    if bcc_recipients:
        all_recipients.extend(bcc_recipients)

    # Connect to SMTP server and send email
    try:
        context = ssl.create_default_context()
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, all_recipients, msg.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")


# Example usage
if __name__ == "__main__":
    sender = "your-email@gmail.com"
    password = "your-app-password"  # Use App Passwords for Gmail security
    to_recipients = ["person1@example.com", "person2@example.com"]
    cc_recipients = ["manager@example.com"]
    bcc_recipients = ["admin@example.com"]
    subject = "Test Email with CC and BCC"
    body = "Hello, this is a test email sent using Python with CC and BCC functionality!"
    attachment = None  # Replace with a file path if needed

    send_email(sender, password, to_recipients, cc_recipients, bcc_recipients, subject, body, attachment)
