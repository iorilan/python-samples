# forks child proces until type 'q'

import os

def child():
    print ("os.fork return 0 .hello from child", os.getpid())
    os._exit(0) # else goes back to parent loop

def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            print("hello from parent", os.getpid(), newpid)
        if input() == 'q': break

parent()
        