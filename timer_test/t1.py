import sys
from threading import Timer
t = Timer(5.5, lambda: print('spam!'))
t.start()
#message will print after 5.5 seconds