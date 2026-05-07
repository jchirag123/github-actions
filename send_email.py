import smtplib
from email.message import EmailMessage
import os

EMAIL = os.environ['Email']
PASSWORD = os.environ['Email_Password']

msg = EmailMessage()
msg['Subject'] = 'Github Action Email Test'
msg['From'] = EMAIL
msg['To'] = EMAIL

msg.set_content('Hello! Email sent from GitHub Actions.')

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
  smtp.login(EMAIL, PASSWORD)
  smtp.send_message(msg)

print("Email Sent Successfully!")
