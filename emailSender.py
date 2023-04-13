""" This example demonstrate sending a plain text email via Google email account
to a list of email recipients, contained in a file, that has one email per line.
Pre-requisites:
1. Need to configure your sender Google email account with
    1) two-step confirmation
    2) create an app password
2. The tempory email account provided by temp-mail.org was used in this program.
"""

# import email package
from email.message import EmailMessage
import ssl

# Using 'smtplib' module to create an SMTP client session object that
# sends an email to any SMTP server
import smtplib

# Initialize login parms from files in 'sample' folder
path_dir = 'sample'  # relative to the current dir
file_pw = f'{path_dir}/email_password.txt'
file_sender = f'{path_dir}/email_sender.txt'
file_receiver = f'{path_dir}/email_list.txt'
file_text = f'{path_dir}/test.txt'

with open(file_pw, 'r') as f:
    email_password = f.read()

with open(file_sender, 'r') as f:
    email_sender = f.read()

with open(file_receiver, 'r') as f:
    # Read in as a tring, stripping off leading and trailing spaces and '\n'
    emails_str = f.read().strip()

    # Split into a list, with one email per element
    recipients = emails_str.split("\n")

with open(file_text, 'r') as f:
    body = f.read()

subject = f'The Contents of {file_text}'

# Compose an text/plain email
em = EmailMessage()
em['From'] = email_sender
em['To'] = ", ".join(recipients)


# Unknown reason? as to why the subject string is not shown on the receiver side
em['Subject'] = subject
em.set_content(body)

# Create SMTP connection
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)

    try:
        smtp.sendmail(email_sender, recipients, em.as_string())
        print(f'An email sent by {email_sender}')
        print(f'===>Check the email from {recipients}')
        print(f'===>Subject={subject}\n')

    except SMTPException:
        print(f'Error: Unable to send email .\n')
