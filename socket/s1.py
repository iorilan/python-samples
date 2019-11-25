from socket import socket ,AF_INET, SOCK_STREAM

port = 50008
host = 'localhost'

def server():
    sock = socket(AF_INET, SOCK_STREAM) # ip addresses tcp connection
    sock.bind(('', port)) # bind to port on this machine
    sock.listen(5) # allow up to 5 pending clients
    while True:
        conn, addr = sock.accept() # wait for client to connect
        data = conn.recv(1024) # read bytes data from this client
        reply = 'server got: [%s]' % data # conn is a new connected socket
        print (reply)
        conn.send('server reply'.encode()) # send bytes reply back to client
def client(name):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((host, port)) # connect to a socket port
    sock.send(name.encode()) # send bytes data to listener
    reply = sock.recv(1024) # receive bytes data from listener
    sock.close() # up to 1024 bytes in message
    print('client got: [%s]' % reply)

if __name__ == '__main__':
    from threading import Thread
    sthread = Thread(target=server)
    sthread.daemon = True # don't wait for server thread
    sthread.start() # do wait for children to exit
    for i in range(5):
        Thread(target=client, args=('client%s' % i,)).start()