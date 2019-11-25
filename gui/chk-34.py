#checkbox demo 2
from tkinter import *
states = [] # change object not name
def onPress(i): # keep track of states
    states[i] = not states[i] # changes False->True, True->False
    print(states)
root = Tk()
for i in range(10):
    chk = Checkbutton(root, text=str(i), command=(lambda i=i: onPress(i)) )
    chk.pack(side=LEFT)
    states.append(False)
root.mainloop()
