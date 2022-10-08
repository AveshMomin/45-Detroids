import imaplib
import email
import imp
from password import password,Email

EMAIL = Email
PASSWORD = password
PORT = 465
SERVER ="smtp.gmail.com"

imap = imaplib.IMAP4_SSL(SERVER)
imap.login(EMAIL,PASSWORD)

imap.select("Inbox")
_, msgnums= imap.search(None,"ALL")
for msgnum in msgnums[0].split():
    _, data = imap.fetch(msgnum, "(RFC822)")
    message = email.message_from_bytes(data[0][1])
    print(f"message num: {msgnum}")
    print(f"From: {message.get('From')}")
    print(f"To: {message.get('To')}")
    print(f"BCC: {message.get('BCC')}")
    print(f"Date: {message.get('Date')}")
    print(f"Subject: {message.get('Subject')}")
    print("Content: ")
    for part in message.walk():
        if part.get_content_type() =="text/plain":
            print(part.as_string())

imap.close()


