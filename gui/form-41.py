from tkinter import *
from quitter import Quitter
demoModules = ['demoDlg-21', 'demoCheck-33', 'demoRadio-36', 'demoScale-39']
parts = []

def addComponents(root):
    for demo in demoModules:
        module = __import__(demo) # import by name string
        part = module.Demo(root) # attach an instance
        part.config(bd=2, relief=GROOVE) # or pass configs to Demo()
        part.pack(side=LEFT, expand=YES, fill=BOTH) # grow, stretch with window
        parts.append(part) # change list in-place
def dumpState():
    for part in parts: # run demo report if any
        print(part.__module__ + ':', end=' ')
        if hasattr(part, 'report'):
            part.report()
        else:
            print('none')
root = Tk() # make explicit root first
root.title('Frames')
Label(root, text='Multiple Frame demo', bg='white').pack()
Button(root, text='States', command=dumpState).pack(fill=X)
Quitter(root).pack(fill=X)
addComponents(root)
root.mainloop()