import os, sys
from tkinter import *
from PIL.ImageTk import PhotoImage

imgdir = ''
imgfile = 'p1.jpg' # does gif, jpg, png, tiff, etc.
if len(sys.argv) > 1:
    imgfile = sys.argv[1]
imgpath = os.path.join(imgdir, imgfile)

win = Tk()
win.title(imgfile)
imgobj = PhotoImage(file=imgpath) # now JPEGs work!
Label(win, image=imgobj).pack()
win.mainloop()
print(imgobj.width(), imgobj.height())