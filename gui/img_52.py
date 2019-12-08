import os, sys
from tkinter import *
from PIL.ImageTk import PhotoImage # <== required for JPEGs and others

imgdir = 'D:\\Craft\\Git\\2019\\python-rd\\gui\\'
if len(sys.argv) > 1: 
    imgdir = sys.argv[1]
imgfiles = os.listdir(imgdir) # does not include directory prefix

main = Tk()
main.title('Viewer')
quit = Button(main, text='Quit all', command=main.quit, font=('courier', 25))
quit.pack()
savephotos = []

for imgfile in imgfiles:
    imgpath = os.path.join(imgdir, imgfile)
    win = Toplevel()
    try:
        win.title(imgfile)
        imgobj = PhotoImage(file=imgpath)
        Label(win, image=imgobj).pack()
        print(imgpath, imgobj.width(), imgobj.height()) # size in pixels
        savephotos.append(imgobj) # keep a reference
    except:
        win.destroy();
        errmsg = 'skipping %s\n%s' % (imgfile, sys.exc_info()[1])
        print(errmsg)
        
        #Label(win, text=errmsg).pack()

main.mainloop()