import ssl
import smtplib
import password

EMAIL = input("Enter your email")
PASSWORD = password
send_to = input("Enter the receiver address here: ")
subject= input("ENter your Subject here:")
content = input("enter your message here")

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com' , 465, context=context) as smtp:
    smtp.login(EMAIL,PASSWORD)
    smtp.sendmail(EMAIL, send_to, msg=f"{subject}\n\n{content}")
