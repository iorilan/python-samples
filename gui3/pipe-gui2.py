# GUI reader side: like pipes-gui1, but make root window and mainloop explicit

from tkinter import *
from gui_redirect_stream import redirectedGuiShellCmd

def launch():
    redirectedGuiShellCmd('python -u pipe-nongui.py')

window = Tk()
Button(window, text='GO!', command=launch).pack()
window.mainloop()
