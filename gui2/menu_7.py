from tkinter import *
root = Tk()
mbutton = Menubutton(root, text='Ations') # the pull-down stands alone
picks = Menu(mbutton)
mbutton.config(menu=picks)
picks.add_command(label='New', command=root.quit)
picks.add_command(label='Edit', command=root.quit)
picks.add_command(label='Delete', command=root.quit)
mbutton.pack()
mbutton.config(bg='white', bd=4, relief=RAISED)
root.mainloop()