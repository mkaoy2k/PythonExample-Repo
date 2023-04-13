""" This example demonstrate sending an email via Google email account
with plain text and alternative html parts.
Pre-requisites:
1. Need to configure your sender Google email account with
    1) two-step confirmation
    2) create an app password
2. The tempory email account provided by temp-mail.org was used in this program.
"""

# Import email packages
import email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import ssl

# Using 'smtplib' module to create an SMTP client session object that sends an email to any SMTP server
import smtplib

# Initialize login parms from files in 'sample' folder
path_dir = 'sample'  # relative to the current dir
file_pw = f'{path_dir}/email_password.txt'
file_sender = f'{path_dir}/email_sender.txt'
file_receiver = f'{path_dir}/email_receiver.txt'
file_text = f'{path_dir}/test.txt'
file_html = f'{path_dir}/test.html'

with open(file_pw, 'r') as f:
    email_password = f.read()
with open(file_sender, 'r') as f:
    email_sender = f.read()
with open(file_receiver, 'r') as f:
    email_receiver = f.read()
with open(file_text, 'r') as f:
    text = f.read()
with open(file_html, 'r') as f:
    html = f.read()

subject = f'The Contents of {file_html}'

# Compose the email object combines these into a signle email message with
# two alternative rendering options.
em = MIMEMultipart("alternative")
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject

# Compose Text part
part1 = MIMEText(text, "plain")

# Compose HTML part
part2 = MIMEText(html, "html")

# Add plain and html parts to MIMEMultipart message
# The recipiant client will try to render the last part first
em.attach(part1)
em.attach(part2)

# Create SMTP connection
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)

    # Send out the email
    try:
        smtp.sendmail(email_sender, email_receiver, em.as_string())
        print(f'An email sent by {email_sender}')
        print(f'===>Check the email from {email_receiver}')
        print(f'===>Subject={subject}\n')

    except SMTPException:
        print(f'Error: Unable to send email .\n')
