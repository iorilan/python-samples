#independent windows

import tkinter
from tkinter import Tk, Button
tkinter.NoDefaultRoot()
win1 = Tk() # two independent root windows
win2 = Tk()
Button(win1, text='[First]', command=win1.destroy).pack()
Button(win2, text='[2nd]', command=win2.destroy).pack()
win1.mainloop()