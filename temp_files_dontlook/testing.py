import tkinter as tk
from tkinter import *


root = tk.Tk()

entr = Entry(root)
entr.pack()

def char_limiter_entry(e):
    s = entr.get().strip()
    s = s[-1] if s in range(0,20) else ''
    entr.delete ('20',END)
    entr.insert(INSERT,s)

def char_limiter_deleter(e):
    entr2.delete ('0',END)


entr.bind('<KeyRelease>', char_limiter_entry)


entr2 = Entry(root)
entr2.pack()



entr2.bind('<KeyPress>',char_limiter_deleter)



root.mainloop()