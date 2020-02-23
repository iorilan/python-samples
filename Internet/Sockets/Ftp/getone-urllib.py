
import os, getpass
from urllib.request import urlopen       # socket-based web tools
filename = 'file.jpg'                 # remote/local filename
password = getpass.getpass('Pswd?')

remoteaddr = 'ftp://username:%s@ftp.file.net/%s;type=i' % (password, filename)
print('Downloading', remoteaddr)

# this works too:
# urllib.request.urlretrieve(remoteaddr, filename)

remotefile = urlopen(remoteaddr)                 # returns input file-like object
localfile  = open(filename, 'wb')                # where to store data locally
localfile.write(remotefile.read())
localfile.close()
remotefile.close()
