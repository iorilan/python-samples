
# run even if no threads                 # in standard lib now
try:                                     # raise ImportError to
    import _thread as thread             # run with GUI blocking
except ImportError:                      # if threads not available
    import _dummy_thread as thread       # same interface, no threads

# shared cross-process queue
# named in shared global scope, lives in shared object memory 
import queue, sys
threadQueue = queue.Queue(maxsize=0)              # infinite size

def threadChecker(widget, delayMsecs=100, perEvent=1):       # 10x/sec, 1/timer
    for i in range(perEvent):                                # pass to set speed
        try:                                                
            (callback, args) = threadQueue.get(block=False)  # run <= N callbacks
        except queue.Empty:
            break                                            # anything ready?
        else:
            callback(*args)                                  # run callback here

    widget.after(delayMsecs,                                 # reset timer event
        lambda: threadChecker(widget, delayMsecs, perEvent)) # back to event loop


def threaded(action, args, context, onExit, onFail, onProgress):
    try:
        if not onProgress:            # wait for action in this thread
            action(*args)             # assume raises exception if fails
        else:
            def progress(*any):
                threadQueue.put((onProgress, any + context))
            action(progress=progress, *args)
    except:
        threadQueue.put((onFail, (sys.exc_info(), ) + context))
    else:
        threadQueue.put((onExit, context))

def startThread(action, args, context, onExit, onFail, onProgress=None):
    thread.start_new_thread(
        threaded, (action, args, context, onExit, onFail, onProgress))


class ThreadCounter:
    def __init__(self):
        self.count = 0
        self.mutex = thread.allocate_lock()     # or use Threading.semaphore
    def incr(self):
        self.mutex.acquire()                    # or with self.mutex: 
        self.count += 1
        self.mutex.release()
    def decr(self):
        self.mutex.acquire()
        self.count -= 1
        self.mutex.release()
    def __len__(self): return self.count        # True/False if used as a flag


if __name__ == '__main__':                      # self-test code when run
    import time                                 # or PP4E.Gui.Tour.scrolledtext
    from tkinter.scrolledtext import ScrolledText

    def onEvent(i):                             # code that spawns thread
        myname = 'thread-%s' % i
        startThread(
            action     = threadaction,
            args       = (i, 3),
            context    = (myname,),
            onExit     = threadexit,
            onFail     = threadfail,
            onProgress = threadprogress)

    # thread's main action
    def threadaction(id, reps, progress):       # what the thread does
        for i in range(reps):
            time.sleep(1)
            if progress: progress(i)            # progress callback: queued
        if id % 2 == 1: raise Exception         # odd numbered: fail

    # thread exit/progress callbacks: dispatched off queue in main thread
    def threadexit(myname):
        text.insert('end', '%s\texit\n' % myname)
        text.see('end')

    def threadfail(exc_info, myname):
        text.insert('end', '%s\tfail\t%s\n' % (myname, exc_info[0]))
        text.see('end')

    def threadprogress(count, myname):
        text.insert('end', '%s\tprog\t%s\n' % (myname, count))
        text.see('end')
        text.update()   # works here: run in main thread


    text = ScrolledText()
    text.pack()
    threadChecker(text)                 # start thread loop in main thread
    text.bind('<Button-1>',             # 3.x need list for map, range ok
              lambda event: list(map(onEvent, range(6))) )
    text.mainloop()                     # pop-up window, enter tk event loop
