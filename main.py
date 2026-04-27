import tkinter as tk
from tkinter import *
import tkinter.messagebox as messagebox
import re
from clients import init_db, add_client, validate_client

init_db()


root = tk.Tk()
root.title("Login Form")
root.geometry("350x300")
root.config(bg="#f0f0f0")
root.resizable(False,False)

username_var = tk.StringVar()
password_var = tk.StringVar()
show_password = tk.BooleanVar(value=False)
remember_me = tk.BooleanVar()
#register info
firstname_var = tk.StringVar()
lastname_var = tk.StringVar()
patronym_var = tk.StringVar()
birthdate_var = tk.StringVar()
phonenum_var = tk.StringVar()
email_var = tk.StringVar()
newsletter_var = tk.BooleanVar(value=True)


def login():
	client = username_var.get()
	pwd = password_var.get()
	if validate_client(client, pwd):
		messagebox.showinfo("Success", "Login successful!")
	else:
		messagebox.showerror("Failed","Invalid username or password.")

def open_register_window():
	reg_window = Toplevel(root)
	reg_window.title("Register Form")
	reg_window.geometry("350x570")
	reg_window.config(bg="#f0f0f0")
	reg_window.resizable(False,False)
	#title
	tk.Label(reg_window, text="Register", font=("Arial", 19, "bold"), bg='#f0f0f0').pack(pady=10)

	
 
	def toggle_password():
		if show_password.get():
			password_entry.config(show="")
		else:
			password_entry.config(show="*")

	def register():
		regex_email = r'/^[\w\-\.]+@([\w-]+\.)+[\w-]{2,}$/gm'
		regex_birthdate = r'/^(\d{2}[\/.-]\d{2}[\/.-]\d{4}|\d{4}[\/.-]\d{2}[\/.-]\d{2})$/gm'

		client = username_var.get()
		pwd = password_var.get()
		fname = firstname_var.get()
		lname = lastname_var.get()
		patr = patronym_var.get()
		bdate = birthdate_var.get()
		phone = phonenum_var.get()
		mail = email_var.get()

		if client == "" or pwd == "" or fname == "" or lname == "" or phone == "":
			messagebox.showerror("Error","Fill all the information.") 
		elif (re.fullmatch(regex_email, mail)):
			messagebox.showerror("Error","Ivalid email.")
		elif (re.fullmatch(regex_birthdate, bdate)):
			messagebox.showerror("Error","Ivalid date of birth.")
		elif add_client(client, pwd, fname, lname, patr, bdate, phone, mail):
			messagebox.showinfo("Success", "Register successful!")	
		else:
			messagebox.showerror("Error","User already exists.")


	#username
	tk.Label(reg_window, text="Username", bg='#f0f0f0').pack(anchor="w", padx=30)
	username_entry = tk.Entry(reg_window, textvariable=username_var, width=30).pack(pady=2)

	#password
	tk.Label(reg_window, text="Password", bg='#f0f0f0').pack(anchor="w", padx=30)
	password_entry = tk.Entry(reg_window, textvariable=password_var, show="*", width=30)
	password_entry.pack(pady=2)

	#show password checkbox
	toggle_btn_pas = tk.Checkbutton(reg_window, text="Show Password", variable=show_password, bg="#f0f0f0", command=toggle_password)
	toggle_btn_pas.pack(anchor="w", padx=30, pady=5)

	#first name
	tk.Label(reg_window, text="First name", bg='#f0f0f0').pack(anchor="w", padx=30)
	firstname_entry = tk.Entry(reg_window, textvariable=firstname_var, width=30).pack(pady=2)

	#last name
	tk.Label(reg_window, text="Last name", bg='#f0f0f0').pack(anchor="w", padx=30)
	lastname_entry = tk.Entry(reg_window, textvariable=lastname_var, width=30).pack(pady=2)

	#patronym
	tk.Label(reg_window, text="Patronym", bg='#f0f0f0').pack(anchor="w", padx=30)
	patronym_entry = tk.Entry(reg_window, textvariable=patronym_var, width=30).pack(pady=2)

	#date of birth
	tk.Label(reg_window, text="Date of birth | Example: DD/MM/YYYY (21/03/2004)", bg='#f0f0f0').pack(anchor="w", padx=30)
	birthdate_entry = tk.Entry(reg_window, textvariable=birthdate_var, width=30).pack(pady=2)

	# phone number
	tk.Label(reg_window, text="Phone number | Example: 79953849927", bg='#f0f0f0').pack(anchor="w", padx=30)
	phonenum_entry = tk.Entry(reg_window, textvariable=phonenum_var, width=30).pack(pady=2)

	# email
	tk.Label(reg_window, text="Email", bg='#f0f0f0').pack(anchor="w", padx=30)
	email_entry = tk.Entry(reg_window, textvariable=email_var, width=30).pack(pady=2)

	#newsletter
	remember_cb = tk.Checkbutton(reg_window, text="Subscribe to our newsletter", variable=newsletter_var, bg="#f0f0f0")
	remember_cb.pack(anchor="w", padx=30)

	#reg button
	tk.Button(reg_window, text="Register", command=register, width=25, bg="#2196f3", fg = "white").pack(pady=8)



def toggle_password():
	if show_password.get():
		password_entry.config(show="")
	else:
		password_entry.config(show="*")


#title
tk.Label(root, text="Login", font=("Arial", 19, "bold"), bg='#f0f0f0').pack(pady=10)

#username
tk.Label(root, text="Username", bg='#f0f0f0').pack(anchor="w", padx=30)
username_entry = tk.Entry(root, textvariable=username_var, width=30).pack(pady=2)

#password
tk.Label(root, text="Password", bg='#f0f0f0').pack(anchor="w", padx=30)
password_entry = tk.Entry(root, textvariable=password_var, show="*", width=30)
password_entry.pack(pady=2)

#show password checkbox
toggle_btn_pas = tk.Checkbutton(root, text="Show Password", variable=show_password, bg="#f0f0f0", command=toggle_password)
toggle_btn_pas.pack(anchor="w", padx=30, pady=5)

#remember me thing
remember_cb = tk.Checkbutton(root, text="Remember me", variable=remember_me, bg="#f0f0f0")
remember_cb.pack(anchor="w", padx=30)

#login n reg buttons
tk.Button(root, text="Login", command=login, width=25, bg="#4caf50", fg = "white").pack(pady=8)
tk.Button(root, text="Register", command=open_register_window, width=25, bg="#2196f3", fg = "white").pack(pady=8)


root.mainloop()