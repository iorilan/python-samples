from tkinter import *
msg = Message(text="RED message box ")
msg.config(bg='red', font=('times', 16, 'italic'))
msg.pack(fill=X, expand=YES)
mainloop()