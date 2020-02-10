
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

class Demo(Frame):
    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.pack()
        Label(self, text ="Basic demos").pack()
        Button(self, text='open', command=self.openfile).pack(fill=BOTH)
        Button(self, text='save', command=self.savefile).pack(fill=BOTH)
        self.open_name = self.save_name = ""
    def openfile(self):                         # save user results
        self.open_name = askopenfilename()      # use dialog options here
    def savefile(self):
        self.save_name = asksaveasfilename(initialdir='C:\\Python31')

if  __name__ == "__main__":
    # display window once
    print('popup1...')
    mydialog = Demo()                # attaches Frame to default Tk()
    mydialog.mainloop()              # display; returns after windows closed
    print(mydialog.open_name)        # names still on object, though GUI gone
    print(mydialog.save_name)
    # Non GUI section of the program uses mydialog here

    # display window again
    print('popup2...')
    mydialog = Demo()              # re-create widgets again
    mydialog.mainloop()            # window pops up again
    print(mydialog.open_name)      # new values on the object again
    print(mydialog.save_name)
    # Non GUI section of the program uses mydialog again
    print('ending...')
