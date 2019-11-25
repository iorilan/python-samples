from tkinter.filedialog import askopenfilename # get standard dialogs
from tkinter.colorchooser import askcolor # they live in Lib\tkinter
from tkinter.messagebox import askquestion, showerror,showinfo
from tkinter.simpledialog import askfloat
demos = {
    'Open': lambda :showinfo("your selection:",askopenfilename()),
    'Color': lambda :showinfo("your selection:",askcolor()),
    'Query': lambda: showinfo("your answer:",askquestion('Warning', 'Warning. Proceed?')),
    'Error': lambda: showerror('Error!', "Fatal error"),
    'Input': lambda: showinfo("you keyed in:",askfloat('Entry', 'Enter credit card number'))
}