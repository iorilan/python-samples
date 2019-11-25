#button sample
#click to exit

# import sys
# from tkinter import *
# widget = Button(None, text='Hello widget world', command=sys.exit)
# widget.pack()
# widget.mainloop()


#button position left
# from tkinter import *
# root = Tk()
# Button(root, text='press', command=root.quit).pack(side=LEFT)
# root.mainloop()

#center button
# from tkinter import *
# root = Tk()
# Button(root, text='press', command=root.quit).pack(side=LEFT, expand=YES)
# root.mainloop()


#button position right
# from tkinter import *
# root = Tk()
# Button(root, text='press', command=root.quit).pack(side=RIGHT)
# root.mainloop()

#button fill 
from tkinter import *
root = Tk()
Button(root, text='press', command=root.quit).pack(side=LEFT, expand=YES, fill=X)
root.mainloop()