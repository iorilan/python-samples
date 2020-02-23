

import smtplib, sys, email.utils, mailconfig,getpass, ssl
mailserver = mailconfig.smtpservername         # ex: smtp.rmi.net

From = input('From? ').strip()                 # or import from mailconfig
pwd = getpass.getpass('Password for %s?' % From)
To   = input('To?   ').strip()                 # ex: python-list@python.org
Tos  = To.split(';')                           # allow a list of recipients
Subj = input('Subj? ').strip()
Date = email.utils.formatdate()                # curr datetime, rfc2822

# standard headers, followed by blank line, followed by text
text = ('From: %s\nTo: %s\nDate: %s\nSubject: %s\n\n' % (From, To, Date, Subj))

print('Type message text, end with line=[Ctrl+d (Unix), Ctrl+z (Windows)]')
while True:
    line = sys.stdin.readline()
    if not line: 
        break                        # exit on ctrl-d/z
   #if line[:4] == 'From':
   #    line = '>' + line            # servers may escape
    text += line

print('Connecting...', mailserver)
#server = smtplib.SMTP(mailserver)      
#context = ssl.create_default_context()
#connection = smtplib.SMTP('smtp-mail.outlook.com', 587)
with smtplib.SMTP(mailserver, 25) as server:
    server.connect(mailserver,25)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(From, pwd)        # connect, no log-in step
    failed = server.sendmail(From, Tos, text)
    server.quit()
    if failed:                                     # smtplib may raise exceptions
        print('Failed recipients:', failed)        # too, but let them pass here
    else:
        print('No errors.')
    print('Bye.')
