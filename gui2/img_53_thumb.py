import os, sys, math
from tkinter import *
from PIL import Image # <== required for thumbs
from PIL.ImageTk import PhotoImage # <== required for JPEG display

def makeThumbs(imgdir, size=(100, 100), subdir='thumbs'):
    thumbdir = os.path.join(imgdir, subdir)
    if not os.path.exists(thumbdir):
        os.mkdir(thumbdir)

    thumbs = []
    included_extensions = ['jpg','jpeg', 'bmp', 'png', 'gif']
    files = [imgfile for imgfile in os.listdir(imgdir) if any(imgfile.endswith(ext) for ext in included_extensions)]

    for imgfile in files :
    #for imgfile in os.listdir(imgdir):
        thumbpath = os.path.join(thumbdir, imgfile)
        if os.path.exists(thumbpath):
            print (thumbpath, '[exists]')
            try:
                thumbobj = Image.open(thumbpath) # use already created
                thumbs.append((imgfile, thumbobj))
            except:
                print ('failed to open ', thumbpath)
        else:
            print('making', thumbpath)
            imgpath = os.path.join(imgdir, imgfile)
            try:
                imgobj = Image.open(imgpath) # make new thumb
                imgobj.thumbnail(size, Image.ANTIALIAS) # best downsize filter
                imgobj.save(thumbpath) # type via ext or passed
                thumbs.append((imgfile, imgobj))
            except: # not always IOError
                print("Skipping: ", imgpath)
    return thumbs
class ViewOne(Toplevel):
    def __init__(self, imgdir, imgfile):
        Toplevel.__init__(self)
        self.title(imgfile)
        imgpath = os.path.join(imgdir, imgfile)
        imgobj = PhotoImage(file=imgpath)
        Label(self, image=imgobj).pack()
        print(imgpath, imgobj.width(), imgobj.height()) # size in pixels
        self.savephoto = imgobj # keep reference on me

def viewer(imgdir, kind=Toplevel, cols=None):
    win = kind()
    win.title('Viewer: ' + imgdir)
    quit = Button(win, text='Quit', command=win.quit, bg='beige') # pack first
    quit.pack(fill=X, side=BOTTOM) # so clip last
    thumbs = makeThumbs(imgdir)
    if not cols:
        cols = int(math.ceil(math.sqrt(len(thumbs)))) # fixed or N x N
    savephotos = []

    while thumbs:
        thumbsrow, thumbs = thumbs[:cols], thumbs[cols:]
        row = Frame(win)
        row.pack(fill=BOTH)
        for (imgfile, imgobj) in thumbsrow:
            photo = PhotoImage(imgobj)
            link = Button(row, image=photo)
            handler = lambda savefile=imgfile: ViewOne(imgdir, savefile)
            link.config(command=handler)
            link.pack(side=LEFT, expand=YES)
            savephotos.append(photo)
    return win, savephotos

if __name__ == '__main__':
    imgdir = (len(sys.argv) > 1 and sys.argv[1]) or 'D:\\Tmp'
    main, save = viewer(imgdir, kind=Tk)
    main.mainloop()