import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path 

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Senders Name'
email['to'] = '<send_to_email>'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'Name'}), 'html')

try:
    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('senders_email', 'senders_password')
        smtp.send_message(email)
        print('all good boss!')
except:
    print('Something went wrong')