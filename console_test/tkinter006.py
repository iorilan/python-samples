from tkinter import *
from tkinter.messagebox import showinfo

def reply(name):
    showinfo(title='Reply', message='Hello %s!' %name)

frame=Tk()
frame.title('Echo')
#frame.iconbitmap('py-blue-trans-out.ico')

Label(frame, text='enter your name:').pack(side=TOP)
ent = Entry(frame)
ent.pack(side=TOP)
btn = Button(frame, text='submit', command=(lambda: reply(ent.get())))
btn.pack(side=LEFT)

frame.mainloop()
