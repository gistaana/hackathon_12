from create_email_template import create_email_template
import time
import os
import ssl
import smtplib
from email.message import EmailMessage
from db_connection import FirebaseConnection

sender = 'encouragingreminders2023@gmail.com'
password = 'wbuhfzguowizlode'

FC = FirebaseConnection()
email_list = FC.get_all_email_data()
delay = 60

while True:    
    for email in email_list:
        receiver = email.get("email", "")

        subject_line = 'Hey! Just wanted to remind you that...'
        body = create_email_template(receiver)
        email = EmailMessage()
        email['From'] = sender
        email['To'] = receiver
        email['Subject'] = subject_line
        email.set_content(body)
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(sender, password)
            smtp.sendmail(sender, receiver, email.as_string())

    print("Emails sent!")
    time.sleep(delay)

