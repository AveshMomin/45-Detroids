import email
import imp
import smtplib
import ssl
from unittest import result
import pandas as pd
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path
from password import password,Email
from datetime import date 

PORT = 465
SERVER ="smtp.gmail.com"
EMAIL = Email
PASSWORD = password
SHEET_NAME = "Sheet Name"
SHEET_ID ="Your id here"
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

def load_df(url):
    parse_dates = ["schedule_date","final_date"]
    df = pd.read_csv(url, parse_dates=parse_dates)
    return df

def query_data_and_send_emails(df):
    present = date.today()
    email_counter = 0
    for _, row in df.iterrows():
        if(present >= row["schedule_date"].date()):
            send_email(
            reciever_email=row["email"],
            name=row["name"],
            subject=row["subject"],
            scheduled_date= row["schedule_date"].strftime("%d, %b %Y")
         )
        email_counter += 1
    return f"Total email sent: {email_counter}"

def send_email(reciever_email ,name ,subject ,scheduled_date):
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = reciever_email
    msg.set_content(
        f"""\
        Hi {name},
        This to test the code.
        Enjoy😁.
        """
    ) 
    msg.add_alternative(
        f"""\
            <html>
                <body>
                    <p> Hi {name},</p>
                    <p>This to test the code.</p>
                    <p>Enjoy😁.</p>
                </body>
            </html>
        """,
            subtype ="html",
    )
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SERVER , PORT,  context=context) as smtp:
        smtp.login(EMAIL,PASSWORD)
        smtp.sendmail(EMAIL, reciever_email, msg.as_string())


df = load_df(URL)
result = query_data_and_send_emails(df)
print(result)

   

