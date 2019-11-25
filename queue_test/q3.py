#a sample of producer and consumer pattern

numconsumers = 2
numproducers = 4
nummessages = 4

import threading,queue ,time
dataQueue = queue.Queue()

def producer(idnum):
    for msgnum in range(nummessages):
        time.sleep(idnum)
        dataQueue.put('[producer id=%d, count=%d]' % (idnum, msgnum))

def consumer(idnum):
    while True:
        time.sleep(0.1)
        try:
            data = dataQueue.get(block=False)
        except queue.Empty:
            pass
        else:
            print('consumer', idnum, 'got =>', data)

if __name__ == '__main__':
    for i in range(numconsumers):
        t = threading.Thread(target=consumer, args=(i,))
        t.daemon = True
        t.start()

    waitfor = []
    for i in range(numproducers):
        t = threading.Thread(target=producer, args=(i,))
        waitfor.append(t)
        t.start()
    
    for t in waitfor: t.join()
    #time.sleep(((numproducers-1)*nummessages)+1)
    print('main thread exit')