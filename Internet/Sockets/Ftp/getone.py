import sys
from getpass import getpass                   # hidden password input
from ftplib import FTP                        # socket-based FTP tools

nonpassive  = False                           # force active mode FTP for server?
filename    = 'filename.jpg'                   # file to be downloaded
dirname     = '.'                             # remote directory to fetch from
sitename    = 'ftp.file.net'                   # FTP site to contact
userinfo    = ('username', getpass('Pswd?'))      # use () for anonymous
if len(sys.argv) > 1: filename = sys.argv[1]  # filename on command line?

print('Connecting...')
connection = FTP(sitename)                  # connect to FTP site
connection.login(*userinfo)                 # default is anonymous login
connection.cwd(dirname)                     # xfer 1k at a time to localfile
if nonpassive:                              # force active FTP if server requires
    connection.set_pasv(False)

print('Downloading...')
localfile = open(filename, 'wb')            # local file to store download
connection.retrbinary('RETR ' + filename, localfile.write, 1024)
connection.quit()
localfile.close()

if input('Open file?') in ['Y', 'y']:
    from playfile import playfile
    playfile(filename)
