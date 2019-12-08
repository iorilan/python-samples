import sys, math
from tkinter import *
from PIL.ImageTk import PhotoImage
from img_53_thumb import makeThumbs, ViewOne
def viewer(imgdir, kind=Toplevel, numcols=None, height=300, width=300):
    
    win = kind()
    win.title('Simple viewer: ' + imgdir)
    quit = Button(win, text='Quit', command=win.quit, bg='beige')
    quit.pack(side=BOTTOM, fill=X)
    canvas = Canvas(win, borderwidth=0)
    vbar = Scrollbar(win)
    hbar = Scrollbar(win, orient='horizontal')
    vbar.pack(side=RIGHT, fill=Y) # pack canvas after bars
    hbar.pack(side=BOTTOM, fill=X) # so clipped first
    canvas.pack(side=TOP, fill=BOTH, expand=YES)
    vbar.config(command=canvas.yview) # call on scroll move
    hbar.config(command=canvas.xview)
    canvas.config(yscrollcommand=vbar.set) # call on canvas move
    canvas.config(xscrollcommand=hbar.set)
    canvas.config(height=height, width=width) # init viewable area size
    # changes if user resizes
    thumbs = makeThumbs(imgdir) # [(imgfile, imgobj)]
    numthumbs = len(thumbs)
    if not numcols:
        numcols = int(math.ceil(math.sqrt(numthumbs))) # fixed or N x N
    numrows = int(math.ceil(numthumbs / numcols)) # 3.x true div

    linksize = max(thumbs[0][1].size) # (width, height)
    fullsize = (0, 0, # upper left X,Y
        (linksize * numcols), (linksize * numrows) ) # lower right X,Y
    canvas.config(scrollregion=fullsize) # scrollable area size

    rowpos = 0
    savephotos = []
    while thumbs:
        thumbsrow, thumbs = thumbs[:numcols], thumbs[numcols:]
        colpos = 0
        for (imgfile, imgobj) in thumbsrow:
            photo = PhotoImage(imgobj)
            link = Button(canvas, image=photo)
            handler = lambda savefile=imgfile: ViewOne(imgdir, savefile)
            link.config(command=handler, width=linksize, height=linksize)
            link.pack(side=LEFT, expand=YES)
            canvas.create_window(colpos, rowpos, anchor=NW,window=link, width=linksize, height=linksize)
            colpos += linksize
            savephotos.append(photo)
        rowpos += linksize
    return win, savephotos
if __name__ == '__main__':
    imgdir = 'images' if len(sys.argv) < 2 else sys.argv[1]
    main, save = viewer(imgdir, kind=Tk)
    main.mainloop()