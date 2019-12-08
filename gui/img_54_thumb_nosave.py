import os, sys
from PIL import Image
from tkinter import Tk
import img_53_thumb as viewer_thumbs
def makeThumbs(imgdir, size=(100, 100), subdir='thumbs'):
    thumbs = []
    included_extensions = ['jpg','jpeg', 'bmp', 'png', 'gif']
    files = [imgfile for imgfile in os.listdir(imgdir) if any(imgfile.endswith(ext) for ext in included_extensions)]
    for imgfile in files :
        imgpath = os.path.join(imgdir, imgfile)
        try:
            imgobj = Image.open(imgpath) # make new thumb
            imgobj.thumbnail(size)
            thumbs.append((imgfile, imgobj))
        except:
            print("Skipping: ", imgpath)
    return thumbs

if __name__ == '__main__':
    imgdir = (len(sys.argv) > 1 and sys.argv[1]) or 'D:\\Tmp'
    viewer_thumbs.makeThumbs = makeThumbs
    main, save = viewer_thumbs.viewer(imgdir, kind=Tk)
    main.mainloop()