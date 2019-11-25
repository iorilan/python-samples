import _thread

def child(tid):
    print ("hello from thread", tid)

def parent():
    i = 0
    while True:
        i += 1
        _thread.start_new_thread(child, (i ,
        #what is this shit ? why must tuple ?
        ))
        if input() == 'q':break

parent()
