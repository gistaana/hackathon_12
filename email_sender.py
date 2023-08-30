import os
import ssl
import smtplib
from email.message import EmailMessage

sender = 'encouragingreminders2023@gmail.com'
password = 'wbuhfzguowizlode'
receiver = 'tuk87239@temple.edu'

subject_line = 'Hey! Just wanted to remind you that...'
body = """
Testing. Testing. Can anyone hear me?
"""

email = EmailMessage()
email['From'] = sender
email['To'] = receiver
email['Subject'] = subject_line
email.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(sender, password)
    smtp.sendmail(sender, receiver, email.as_string())