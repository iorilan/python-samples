from tkinter import * # get widget classes
from tkinter.messagebox import * # get canned std dialog
class Quitter(Frame): # subclass our GUI
    def __init__(self, parent=None): # constructor method
        Frame.__init__(self, parent)
        self.pack()
        widget = Button(self, text='Quit', command=self.quit)
        widget.pack(side=LEFT, expand=YES, fill=BOTH)
    def quit(self):
        ans = askokcancel('Verify exit', "Really quit?")
        if ans: Frame.quit(self)
        else: showwarning('Ok', 'Quit has been cancelled')
if __name__ == '__main__': Quitter().mainloop()