from tkinter import * # get base widget set
from glob import glob # filename expansion list
import demoCheck_33 as demoCheck
import random # pick a picture at random

class ButtonPicsDemo(Frame):
    def __init__(self, gifdir="", parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.lbl = Label(self, text="none", bg='blue', fg='red')
        self.pix = Button(self, text="Press me", command=self.draw, bg='white')
        self.lbl.pack(fill=BOTH)
        self.pix.pack(pady=10)
        #demoCheck.Demo(self, relief=SUNKEN, bd=2).pack(fill=BOTH)
        files = glob("*.gif")
        self.images = [(x, PhotoImage(file=x)) for x in files]
        print(files)

    def draw(self):
        name, photo = random.choice(self.images)
        self.lbl.config(text=name)
        self.pix.config(image=photo)
if __name__ == '__main__': ButtonPicsDemo().mainloop()