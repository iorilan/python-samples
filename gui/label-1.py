#hello world

# from tkinter import Label # get a widget object
# widget = Label(None, text='Hello GUI world!') # make one
# widget.pack() # arrange it
# widget.mainloop() # start event loop

#same as above
from tkinter import *
root = Tk()
Label(root, text='Hello GUI world!').pack(side=TOP)
root.mainloop()