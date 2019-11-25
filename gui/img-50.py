import os, sys
from tkinter import * # use standard tkinter photo object
# GIF works, but JPEG requires PIL
imgdir = ''
imgfile = 'p4.png'
if len(sys.argv) > 1: # cmdline argument given?
    imgfile = sys.argv[1]
imgpath = os.path.join(imgdir, imgfile)

win = Tk()
win.title(imgfile)
imgobj = PhotoImage(file=imgpath) # display photo on a Label
Label(win, image=imgobj).pack()
print(imgobj.width(), imgobj.height()) # show size in pixels before destroyed
win.mainloop()