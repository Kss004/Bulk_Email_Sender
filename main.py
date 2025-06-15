import streamlit as st
import os
from app import send_email
import tempfile

st.set_page_config(page_title="Bulk Email Sender", page_icon="📧")

st.title(" Bulk Email Sender")
st.write("Send emails to multiple recipients with attachments")

# Email configuration
with st.form("email_form"):
    # Sender details
    st.subheader("Sender Details")
    sender_email = st.text_input("Your Email (Gmail)", placeholder="your-email@gmail.com")
    sender_password = st.text_input("Your App Password", type="password",
                                    help="Use App Password from Google Account settings for security")

    # Recipients
    st.subheader("Recipients")
    recipients_text = st.text_area("Recipient Email Addresses",
                                   placeholder="Enter email addresses separated by commas",
                                   help="Example: email1@example.com, email2@example.com")

    # Email content
    st.subheader("Email Content")
    subject = st.text_input("Subject")
    
    # Email format selection
    email_format = st.radio(
        "Email Format",
        ["Plain Text", "HTML"],
        help="Choose whether to send as plain text or HTML formatted email"
    )
    
    # Email body based on format
    if email_format == "Plain Text":
        body = st.text_area("Email Body", placeholder="Enter your email content here...")
    else:
        st.markdown("**HTML Email Body**")
        st.markdown("Enter your HTML code below. You can include CSS styling, images, and formatting.")
        body = st.text_area("HTML Email Body", 
                           placeholder="<!DOCTYPE html><html><head><title>Your Email</title></head><body><h1>Hello!</h1><p>Your content here...</p></body></html>",
                           height=400)
        
        # Show HTML preview
        if body:
            st.subheader("HTML Preview")
            st.components.v1.html(body, height=400, scrolling=True)

    # File upload
    st.subheader("Attachments")
    uploaded_files = st.file_uploader("Upload Files", accept_multiple_files=True)

    # Submit button
    submitted = st.form_submit_button("Send Email")

if submitted:
    if not sender_email or not sender_password or not recipients_text or not subject or not body:
        st.error("Please fill in all required fields!")
    else:
        try:
            # Process recipients
            recipients = [email.strip() for email in recipients_text.split(",")]

            # Handle attachments
            attachment_paths = []
            if uploaded_files:
                for uploaded_file in uploaded_files:
                    # Get the original filename and extension
                    original_filename = uploaded_file.name
                    # Create a temporary file with the original filename
                    temp_dir = tempfile.mkdtemp()
                    temp_path = os.path.join(temp_dir, original_filename)

                    with open(temp_path, 'wb') as tmp_file:
                        tmp_file.write(uploaded_file.getvalue())
                        attachment_paths.append(temp_path)

            # Send email
            with st.spinner("Sending email..."):
                send_email(
                    sender_email=sender_email,
                    sender_password=sender_password,
                    recipient_emails=recipients,
                    subject=subject,
                    body=body,
                    email_format=email_format.lower().replace(" ", "_"),
                    attachment_path=attachment_paths[0] if attachment_paths else None
                )
                st.success("Email sent successfully!")

            # Clean up temporary files and directories
            for path in attachment_paths:
                os.unlink(path)  # Remove the temporary file
                os.rmdir(os.path.dirname(path))  # Remove the temporary directory

        except Exception as e:
            st.error(f"Error sending email: {str(e)}")

# Add some helpful information
with st.expander("How to use"):
    st.markdown("""
    1. **Sender Details**:
       - Enter your Gmail address
       - Use an App Password from your Google Account settings (for security)

    2. **Recipients**:
       - Enter email addresses separated by commas
       - Example: email1@example.com, email2@example.com

    3. **Email Content**:
       - Enter the subject and body of your email
       - Choose between Plain Text or HTML format
       - For HTML emails, you can include CSS styling and formatting

    4. **Attachments**:
       - Upload any files you want to attach
       - You can upload multiple files

    5. **Send**:
       - Click the "Send Email" button to send your email
    """)

with st.expander("How to get App Password"):
    st.markdown("""
    1. Go to your Google Account settings
    2. Navigate to Security
    3. Enable 2-Step Verification if not already enabled
    4. Go to App Passwords
    5. Generate a new app password for "Mail"
    6. Use this generated password in the app
    """)

with st.expander("HTML Email Tips"):
    st.markdown("""
    **Best Practices for HTML Emails:**
    
    1. **Use Inline CSS**: Most email clients strip out `<style>` tags, so use inline styles
    2. **Table-based Layout**: Use HTML tables for layout as they're more reliable across email clients
    3. **Responsive Design**: Include viewport meta tag and use responsive CSS
    4. **Image Hosting**: Host images on a public server and use absolute URLs
    5. **Fallback Fonts**: Always specify fallback fonts for better compatibility
    6. **Test Across Clients**: Test your HTML emails in different email clients
    
    **Example HTML Structure:**
    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Your Email Title</title>
    </head>
    <body style="margin: 0; padding: 20px; font-family: Arial, sans-serif;">
        <h1 style="color: #333;">Hello!</h1>
        <p style="color: #666;">Your content here...</p>
    </body>
    </html>
    ```
    """)