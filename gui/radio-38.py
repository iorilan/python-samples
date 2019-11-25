from tkinter import *
state = ''
buttons = []
def onPress(i):
    global state
    state = i
    for btn in buttons:
        btn.deselect()
    buttons[i].select()
    print(state)
root = Tk()
for i in range(10):
    rad = Radiobutton(root, text=str(i),
    value=str(i), command=(lambda i=i: onPress(i)) )
    rad.pack(side=LEFT)
    buttons.append(rad)
onPress(0) # select first initially
root.mainloop()