import tkinter as tk
from tkinter import *
import tkinter.messagebox as messagebox
import re
from clients import init_db, add_client

init_db()
root = tk.Tk()

#register info
username_var = tk.StringVar()
password_var = tk.StringVar()
show_password = tk.BooleanVar(value=False)
firstname_var = tk.StringVar()
lastname_var = tk.StringVar()
patronym_var = tk.StringVar()
birthdate_var = tk.StringVar()
phonenum_var = tk.StringVar()
email_var = tk.StringVar()
newsletter_var = tk.BooleanVar(value=True)

def open_register_window():
	reg_window = Toplevel(root)
	reg_window.title("Register Form")
	reg_window.geometry("350x570")
	reg_window.config(bg="#434D20")
	reg_window.resizable(False,False)
	#title
	tk.Label(reg_window, text="Register", foreground='white', font=("Rockwell Extra Bold", 19, "bold"), bg='#E9839D', ).pack(pady=10)

    def register():
        regex_email = r'^[\w\-\.]+@([\w-]+\.)+[\w-]{2,}$'
        regex_birthdate = r'^(\d{2}[\/.-]\d{2}[\/.-]\d{4}|\d{4}[\/.-]\d{2}[\/.-]\d{2})$'

        client = username_var.get()
        pwd = password_var.get()
        fname = firstname_var.get()
        lname = lastname_var.get()
        patr = patronym_var.get()
        bdate = birthdate_var.get()
        phone = phonenum_var.get()
        mail = email_var.get()

        if client == "" or pwd == "" or fname == "" or lname == "" or phone == "":
            messagebox.showerror("Error", "Fill all the information.")
        elif not re.fullmatch(regex_birthdate, bdate):
            messagebox.showerror("Error", "Ivalid date of birth.")
        elif not re.fullmatch(regex_email, mail):
            messagebox.showerror("Error", "Ivalid email.")
        elif add_client(client, pwd, fname, lname, patr, bdate, phone, mail):
            messagebox.showinfo("Success", "Register successful!")
        else:
            messagebox.showerror("Error", "User already exists.")


    # username
    tk.Label(reg_window, text="Username", foreground='white', font=("Copperplate Gothic Light", 10), bg='#434D20').pack(
        anchor="w", padx=30)
    username_entry_reg = tk.Entry(reg_window, textvariable=username_var, width=30, cursor="target").pack(pady=2)


    def validate_phone(phone):
        if phone.isdigit() or phone == "":
            return True
        return False


    vcmd = reg_window.register(validate_phone)

    # password
    tk.Label(reg_window, text="Password", foreground='white', font=("Copperplate Gothic Light", 10), bg='#434D20').pack(
        anchor="w", padx=30)
    password_entry_reg = tk.Entry(reg_window, textvariable=password_var, show="*", width=30, cursor="target")
    password_entry_reg.pack(pady=2)

    # first name
    tk.Label(reg_window, text="First name", foreground='white', font=("Copperplate Gothic Light", 10), bg='#434D20').pack(
        anchor="w", padx=30)
    fn_entr = tk.Entry(reg_window, textvariable=firstname_var, width=30, cursor="target").pack(pady=2)

    # last name
    tk.Label(reg_window, text="Last name", foreground='white', font=("Copperplate Gothic Light", 10), bg='#434D20').pack(
        anchor="w", padx=30)
    ln_entr = tk.Entry(reg_window, textvariable=lastname_var, width=30, cursor="target").pack(pady=2)

    # patronym
    tk.Label(reg_window, text="Patronym", foreground='white', font=("Copperplate Gothic Light", 10), bg='#434D20').pack(
        anchor="w", padx=30)
    ptr_entr = tk.Entry(reg_window, textvariable=patronym_var, width=30, cursor="target").pack(pady=2)

    # date of birth
    tk.Label(reg_window, text="Date of birth | DD/MM/YYYY", foreground='white', font=("Copperplate Gothic Light", 10),
             bg='#434D20').pack(anchor="w", padx=30)
    dateofbirth_entr = tk.Entry(reg_window, textvariable=birthdate_var, width=30, cursor="target").pack(pady=2)

    # phone number
    tk.Label(reg_window, text="Phone number | Example: 79953849927", foreground='white',
             font=("Copperplate Gothic Light", 10), bg='#434D20').pack(anchor="w", padx=30)
    phonenum_entry = tk.Entry(reg_window, textvariable=phonenum_var, validate="key", validatecommand=(vcmd, '%P'), width=30,
                              cursor="target")
    phonenum_entry.pack(pady=2)

    # email
    tk.Label(reg_window, text="Email", foreground='white', font=("Copperplate Gothic Light", 10), bg='#434D20').pack(
        anchor="w", padx=30)
    email_entr = tk.Entry(reg_window, textvariable=email_var, width=30, cursor="target").pack(pady=2)

    # newsletter
    remember_cb_reg = tk.Checkbutton(reg_window, text="Subscribe to our newsletter", font=("Copperplate Gothic Light", 10),
                                     variable=newsletter_var, bg="#434D20", fg="#E9839D", cursor="heart")
    remember_cb_reg.pack(anchor="w", padx=30)

    # reg button
    tk.Button(reg_window, text="Register", command=register, width=25, cursor="star", font=("Copperplate Gothic Light", 10),
              bg="#E9839D", fg="white").pack(pady=8)