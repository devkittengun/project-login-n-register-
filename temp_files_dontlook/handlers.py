import tkinter as tk
from tkinter import *

root = tk.Tk()

#char limiters !!!
entr = Entry(root, width=30)
entr.pack(pady=2)

#20
def char_limiter_entry_password_entry(e):
    s = password_entry.get().strip()
    s = s[-1] if s in range(0,20) else ''
    password_entry.delete ('20',END)
    password_entry.insert(INSERT,s)

def char_limiter_entry_password_entry_reg(e):
    s = password_entry_reg.get().strip()
    s = s[-1] if s in range(0,20) else ''
    password_entry_reg.delete ('20',END)
    password_entry_reg.insert(INSERT,s)




# 16
def char_limiter_entry_username_entry(e):
    s = username_entry.get().strip()
    s = s[-1] if s in range(0,16) else ''
    username_entry.delete ('16',END)
    username_entry.insert(INSERT,s)

def char_limiter_entry_username_entry_reg(e):
    s = username_entry_reg.get().strip()
    s = s[-1] if s in range(0,16) else ''
    username_entry_reg.delete ('16',END)
    username_entry_reg.insert(INSERT,s)


#30
def char_limiter_entry_fn_entr(e):
    s = fn_entr.get().strip()
    s = s[-1] if s in range(0,30) else ''
    fn_entr.delete ('30',END)
    fn_entr.insert(INSERT,s)

def char_limiter_entry_ln_entr(e):
    s = ln_entr.get().strip()
    s = s[-1] if s in range(0,30) else ''
    ln_entr.delete ('30',END)
    ln_entr.insert(INSERT,s)

def char_limiter_entry_ptr_entr(e):
    s = ptr_entr.get().strip()
    s = s[-1] if s in range(0,30) else ''
    ptr_entr.delete ('30',END)
    ptr_entr.insert(INSERT,s)

#10
def char_limiter_entry_dateofbirth_entr(e):
    s = dateofbirth_entr.get().strip()
    s = s[-1] if s in range(10) else ''
    dateofbirth_entr.delete ('10',END)
    dateofbirth_entr.insert(INSERT,s)

#11
def char_limiter_entry_phonenum_entry(e):
    s = phonenum_entry.get().strip()
    s = s[-1] if s in range(0,11) else ''
    phonenum_entry.delete ('11',END)
    phonenum_entry.insert(INSERT,s)


#45
def char_limiter_entry_email_entr(e):
    s = email_entr.get().strip()
    s = s[-1] if s in range(0,45) else ''
    email_entr.delete ('45',END)
    email_entr.insert(INSERT,s)

entr.bind('<KeyRelease>', char_limiter_entry_20)


# #char limiter 20
# password_entry.bind('<KeyRelease>', char_limiter_entry_password_entry)
# password_entry_reg.bind('<KeyRelease>', char_limiter_entry_password_entry_reg)
#
# #char limiter 16
# username_entry.bind('<KeyRelease>', char_limiter_entry_username_entry)
# username_entry_reg.bind('<KeyRelease>', char_limiter_entry_username_entry_reg)
#
# #char limiter 30
# fn_entr.bind('<KeyRelease>', char_limiter_entry_fn_entr)
# ln_entr.bind('<KeyRelease>', char_limiter_entry_ln_entr)
# ptr_entr.bind('<KeyRelease>', char_limiter_entry_ptr_entr)
#
# #char limiter 10
# dateofbirth_entr.bind('<KeyRelease>', char_limiter_entry_dateofbirth_entr)
#
# #char limiter 11
# phonenum_entry.bind('<KeyRelease>', char_limiter_entry_phonenum_entry)
#
# #char limiter 45
# email_entr.bind('<KeyRelease>', char_limiter_entry_email_entr)

