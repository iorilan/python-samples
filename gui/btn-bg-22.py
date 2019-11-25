from tkinter import *
from tkinter.colorchooser import askcolor
def setBgColor():
        (triple, hexstr) = askcolor()
        if hexstr:
            print(hexstr)
            btn.config(bg=hexstr)
root = Tk()
btn = Button(root, text='Set Background Color', command=setBgColor)
btn.config(height=3, font=('times', 20, 'bold'))
btn.pack(expand=YES, fill=BOTH)
root.mainloop()