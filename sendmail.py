#! /usr/bin/env python

import smtplib
from sys import argv
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.Utils import formatdate
        
sender   = 'email@example.com'
username = ''
password = ''
server   = 'smtp.gmail.com:587'

def send_mail(subject, recipient, body):
    
    msg            = MIMEMultipart()
    msg['From']    = sender
    msg['To']      = recipient
    msg['Date']    = formatdate(localtime=True)
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))

    smtp = smtplib.SMTP(server)
    print('connecetd to server...')
    smtp.starttls()
    smtp.login(username, password)
    print('logged in to server...')
    
    try:
        smtp.sendmail(sender, recipient, msg.as_string())
        print('mail sent...')
    
    except smtplib.SMTPException, smtp_exception:
        print str(smtp_exception)

    smtp.quit()
    
if __name__ == '__main__':
    
    if 3 > len(argv) > 4:
        print('Wrong number of arguments.')
    
    else:
        send_mail(argv[1], argv[2], argv[3])

