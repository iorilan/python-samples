

import poplib, getpass, sys, mailconfig,ssl

mailserver = mailconfig.popservername      
mailuser   = mailconfig.popusername       
mailpasswd = getpass.getpass('Password for %s?' % mailserver)

print('Connecting...')
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
server = poplib.POP3_SSL(mailserver,'995', context=ctx)
server.user(mailuser)                      # connect, log in to mail server
server.pass_(mailpasswd)                   # pass is a reserved word

try:
    print(server.getwelcome())             # print returned greeting message
    msgCount, msgBytes = server.stat()
    print('There are', msgCount, 'mail messages in', msgBytes, 'bytes')
    print(server.list())
    print('-' * 80)
    input('[Press Enter key]')

    for i in range(msgCount):
        hdr, message, octets = server.retr(i+1)    # octets is byte count
        for line in message: print(line.decode())  # retrieve, print all mail
        print('-' * 80)                            # mail text is bytes in 3.x
        if i < msgCount - 1:
           input('[Press Enter key]')              # mail box locked till quit
finally:                                           # make sure we unlock mbox
    server.quit()                                  # else locked till timeout
print('Bye.')
