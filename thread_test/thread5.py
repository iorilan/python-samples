import threading

class Mythread(threading.Thread):

    def __init__(self, myId, count, mutex):
        self.myId = myId
        self.count = count
        self.mutex = mutex
        threading.Thread.__init__(self)

    def run(self):
        for i in range(self.count):
            with self.mutex:
                print("[%s] => %s" % (self.myId, i))

l = threading.Lock()
threads = []
for i in range(10):
    thread = Mythread(i, 100, l)
    thread.start()
    threads.append(thread)


for t in threads:
    t.join()

print('main thread exiting.')