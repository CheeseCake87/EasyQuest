from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP, SMTPException
from ssl import create_default_context


def send_email(
        username: str,
        subject: str,
        email_to: list,
        email_body: str,
        from_name: str,
        send_from: str,
        reply_to: str,
        password: str,
        server: str,
        port: int,
) -> list:
    """
    Sends a plain HTML email.
    """

    html_msg = MIMEText(email_body)
    html_msg.set_type('text/html')
    html_msg.set_param('charset', 'UTF-8')

    msg = MIMEMultipart()
    msg.set_type('multipart/alternative')
    msg['Subject'] = subject
    msg['To'] = ','.join(email_to)
    msg['From'] = f'"{from_name}"' + f'<{send_from}>'
    msg['Reply-To'] = reply_to
    msg['Original-Sender'] = username
    msg.attach(html_msg)

    try:
        with SMTP(server, port) as connection:
            connection.starttls()
            connection.login(username, password)
            connection.sendmail(send_from, email_to, msg.as_string())
    except SMTPException as error:
        return [False, "AUTHENTICATION OR CONNECTION ISSUE", error]

    return [True, "EMAIL SENT", None]


def test_email_server_connection(
        username: str,
        password: str,
        server: str,
        port: int,
) -> bool:
    """
    Used to test the settings of the smtp settings.
    """

    try:
        ssl_context = create_default_context()
        with SMTP(server, port) as connection:
            connection.starttls(context=ssl_context)
            connection.login(username, password)
    except SMTPException:
        return False

    return True
