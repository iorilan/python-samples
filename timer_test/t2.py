from tkinter import Tk
from tkinter.messagebox import showinfo
win = Tk()
win.after(500, lambda: showinfo('Popup','spam'))
win.mainloop()