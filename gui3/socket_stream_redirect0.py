
import sys
from socket import *
port = 50008
host = 'localhost'                       

def redirectOut(port=port, host=host):  
    sock = socket(AF_INET, SOCK_STREAM)  
    sock.connect((host, port))                # caller operates in client mode
    file = sock.makefile('w')                 # file interface: text, bufferred
    sys.stdout = file                         # make prints go to sock.send

def redirectIn(port=port, host=host): 
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port))
    file = sock.makefile('r') # file interface wrapper
    sys.stdin = file # make input come from sock.recv
    return sock # return value can be ignored
    
def redirectBothAsClient(port=port, host=host): 
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port)) # or open in 'rw' mode
    ofile = sock.makefile('w') # file interface: text, buffered
    ifile = sock.makefile('r') # two file objects wrap same socket
    sys.stdout = ofile # make prints go to sock.send
    sys.stdin = ifile # make input come from sock.recv
    return sock

def redirectBothAsServer(port=port, host=host): 
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((host, port)) # caller is listener here
    sock.listen(5)
    conn, addr = sock.accept()
    ofile = conn.makefile('w') # file interface wrapper
    ifile = conn.makefile('r') # two file objects wrap same socket
    sys.stdout = ofile # make prints go to sock.send
    sys.stdin = ifile # make input come from sock.recv
    return conn