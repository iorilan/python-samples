from tkinter import *
from hellopkg import HelloPackage # or get from gui7c--__getattr__ added

frm = Frame()
frm.pack()
Label(frm, text='hello').pack()

part = HelloPackage(frm)
frm.mainloop()