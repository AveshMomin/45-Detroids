import email
import ssl
import smtplib
import password

EMAIL = email
PASSWORD = password
send_to = input("Enter the receiver address here: ")
subject= input("Enter your Subject here:")
content = input("Enter your message here:")

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com' , 465, context=context) as smtp:
    smtp.login(EMAIL,PASSWORD)
    smtp.sendmail(EMAIL, send_to, msg=f"{subject}\n\n{content}")
