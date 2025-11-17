# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
chars = {
    "num": "1234567890",
    "letter": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "special_chars": "!@#$%&*?.,:;()``{[}]_-+=/`\`|~^"
}


# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)
window.resizable(False, False)

# Logo 
canvas = Canvas(width=170, height=170, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(55, 80, image=img)
canvas.grid(row=0, column=1, columnspan=2)

# Website name label
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
# Label
website_entry = Entry(width=50)
website_entry.focus()
website_entry.grid(row=1, column=1, padx=5, pady=5, ipady=2, columnspan=2, sticky="ew")

# Email/username field
email_label = Label(text="Email/Username")
email_label.grid(row=2, column=0)
# Label
email_entry = Entry(width=50)
email_entry.grid(row=2, column=1, pady=5, padx=5, ipady=2, columnspan=2, sticky="ew")

# password label and field
password_label = Label(text="Password")
password_label.grid(row=3, column=0)
# Entry
password_input = Entry()
password_input.grid(row=3, column=1, padx=5, pady=5, ipady=2, sticky="ew")
# Btn
password_gen_btn = Button(text="Generate Password")
password_gen_btn.grid(row=3, column=2, padx=5, ipadx=2, sticky="ew")


# Add password btn
add_btn = Button(text="Add")
add_btn.grid(row=4, column=1, padx=5, pady=5, columnspan=2, sticky="ew")

window.mainloop()