#link function to button

# import sys
# from tkinter import *
# def quit(): # a custom callback handler
#     print('Hello, I must be going...') # kill windows and process
#     sys.exit()
# widget = Button(None, text='Hello event world', command=quit)
# widget.pack()
# widget.mainloop()

#the lambda way. use 'or' to write 2 lines of code. dont do this
import sys
from tkinter import * # lambda generates a function
widget = Button(None, # but contains just an expression
text='Hello event world',
command=(lambda: print('Hello lambda world') or sys.exit()) )
widget.pack()
widget.mainloop()