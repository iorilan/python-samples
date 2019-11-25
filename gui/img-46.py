#use canvas show image
from tkinter import *
win = Tk()
img = PhotoImage(file="p3.gif")
can = Canvas(win)
can.pack(fill=BOTH)
can.create_image(2, 2, image=img, anchor=NW) # x, y coordinates
win.mainloop()