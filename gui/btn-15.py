import sys
from tkinter import Toplevel, Button, Label
win1 = Toplevel() # two independent windows
win2 = Toplevel() # but part of same process
Button(win1, text='[First]Top Level', command=sys.exit).pack()
Button(win2, text='[2nd]Click To Exit', command=sys.exit).pack()
Label(text='[Attach to root]This is a popup').pack() # on default Tk() root window
win1.mainloop()