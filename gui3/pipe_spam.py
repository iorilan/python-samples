from tkinter import Tk
from pipe_gui3 import redirectedGuiShellCmd
root = Tk()
redirectedGuiShellCmd('python -u spam.py', root)
root.mainloop()