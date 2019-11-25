import threading, _thread

def action(i):
    print("action")
    print(i ** 32)

#1
class Mythread(threading.Thread):
    def __init__(self, i):
        self.i = i
        threading.Thread.__init__(self)

    def run(self):
        #print(self.i ** 32)
        #print("Mythread")
        action(self.i)

Mythread(2).start()

#2
t = threading.Thread(target=(lambda: action(2)))
t.start()

#3
_thread.start_new_thread(action, (2,))
