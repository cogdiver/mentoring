from email.mime.text import MIMEText
import smtplib
import logging
import pandas as pd


def send_email(subject, message):
    """
    Sends an email with the specified subject and HTML message content.

    Args:
        subject (str): The subject of the email.
        message (str): The HTML content of the email message.

    Returns:
        None
    """
    try:
        # SMTP server configuration
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587  # TLS port for Gmail SMTP server

        # Email account credentials
        gmail_user = "valentinaarenas2@gmail.com"
        gmail_password = "oaoi qxfh kvcb eqof"

        # List of recipient email addresses
        to_addresses = [
            "valentinaarenas2@gmail.com"
        ]

        # Create a MIMEText object with HTML content
        msg = MIMEText(message, 'html')
        msg['Subject'] = subject
        msg['From'] = gmail_user
        msg['To'] = ', '.join(to_addresses)  # Convert list to comma-separated string

        # Establish connection to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Start TLS encryption
            server.login(gmail_user, gmail_password)
            server.send_message(msg)

    except Exception as e:
        # Log any error that occurs during the email sending process
        error_message = f'Error sending email notifications: {e}'
        logging.error(error_message)


def send_df_email(df, subject, message):
    """
    Sends an email with the DataFrame included as an HTML table without gaps between cells and without the index.

    Args:
        df (pandas.DataFrame): The DataFrame to send.
        subject (str): The email subject.
        message (str): The message content before the table.

    Returns:
        None
    """
    # Convert the DataFrame to HTML without the index
    df_html = df.to_html(index=False, border=0)

    # Modify the <table> tag to add attributes and styles
    df_html = df_html.replace(
        '<table border="0" class="dataframe">',
        '<table border="1" cellspacing="0" cellpadding="5" style="border-collapse: collapse;">'
    )

    # Add inline styles to <th> tags
    df_html = df_html.replace(
        '<th>',
        '<th style="border: 1px solid black; padding: 5px; text-align: left;">'
    )

    # Add inline styles to <td> tags
    df_html = df_html.replace(
        '<td>',
        '<td style="border: 1px solid black; padding: 5px; text-align: left;">'
    )

    # Combine the message and the HTML table
    full_message = f"{message}<br><br>{df_html}"

    # Send the email using the send_email function
    send_email(subject, full_message)


if __name__ == "__main__":
    # Sample DataFrame
    data = {
        f"col_{i+1}": [j for j in range(5)]
        for i in range(5)
    }
    df = pd.DataFrame(data)

    # Email details
    subject = 'Inventory Report'
    message = 'Dear team,<br><br>Please find the updated inventory report below:'

    # Send the email
    send_df_email(df, subject, message)
