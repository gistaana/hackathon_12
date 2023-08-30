from create_email_template import create_email_template
import time
import ssl
import smtplib
from email.message import EmailMessage
from db_connection import FirebaseConnection

sender = 'encouragingreminders2023@gmail.com'
password = 'wbuhfzguowizlode'

delay = 60
FC = FirebaseConnection()

while True:    
    email_list = [{"email": "parthnpatel@temple.edu", "name": "Parth"}]

    for email_data in email_list:
        receiver = email_data.get("email", "")
        name = email_data.get("name", "")

        subject_line = 'Hey! Just wanted to remind you that...'
        body = create_email_template(receiver, name)
        
        email = EmailMessage()
        email['From'] = sender
        email['To'] = receiver
        email['Subject'] = subject_line
        email.set_content(body, subtype='html')

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(sender, password)
            smtp.sendmail(sender, receiver, email.as_string())

    print("Emails sent!")
    time.sleep(delay)

