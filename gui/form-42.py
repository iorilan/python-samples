from tkinter import *
demoModules = ['demoDlg-21', 'demoRadio-36', 'demoCheck-33', 'demoScale-39']
def makePopups(modnames):
    demoObjects = []
    for modname in modnames:
        module = __import__(modname) # import by name string
        window = Toplevel() # make a new window
        demo = module.Demo(window) # parent is the new window
        window.title(module.__name__)
        demoObjects.append(demo)
    return demoObjects
def allstates(demoObjects):
    for obj in demoObjects:
        if hasattr(obj, 'report'):
            print(obj.__module__, end=' ')
            obj.report()

root = Tk() # make explicit root first
root.title('Popups')
demos = makePopups(demoModules)
Label(root, text='Multiple Toplevel window demo', bg='white').pack()
Button(root, text='States', command=lambda: allstates(demos)).pack(fill=X)
root.mainloop()