import ssl
import smtplib
from password import password,Email
from email.message import EmailMessage
from email.utils import formataddr

EMAIL = Email
PASSWORD = password
PORT = 465
SERVER ="smtp.gmail.com"
reciever_email = input("Enter the receiver address here: ")
subject= input("Enter your Subject here:")

def send_email(reciever_email ,subject ):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = reciever_email
    msg.set_content(
        f"""\
        message content here
        """
    ) 
    msg.add_alternative(
        f"""\
            <html>
                <body>
                    <p> message content here </p>
                </body>
            </html>
        """,
            subtype ="html",
    )
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SERVER , PORT,  context=context) as smtp:
        smtp.login(EMAIL,PASSWORD)
        smtp.sendmail(EMAIL, reciever_email, msg.as_string())

send_email(reciever_email,subject)