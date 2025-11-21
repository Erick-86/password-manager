# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
chars = {
    "num": "1234567890",
    "upper_letters": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "lower_letters": "abcdefghijklmnopqrstuvwxyz",
    "special_chars": "!@#$%&*?.,:;()``{[}]_-+=/`\\`|~^"
}

def password_generator():
    password_len = random.randint(8, 32)
    password = []

    while not len(password) == password_len:
        character_key = random.choice(list(chars.keys()))
        char = random.choice(chars[character_key])
        password.append(char)

    password = "".join(password)
    password_input.delete(0, "end")
    password_input.insert(0, password)

    # copy to clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    # checking for input validation
    entry_lists = [website_entry, password_input, email_entry]
    empty_entry = False
    FILE_PATH = "../mypass.txt"
    for entry in entry_lists:
        if not entry.get():
            messagebox.showerror("Oops", "Please dont leave any field empty")
            empty_entry = True
    if not empty_entry:
        continue_message = messagebox.askyesno("Continue", f"Email: {email_entry.get()}\nPassword: {password_input.get()}\nIs this OK?")

        # Saving data to a text file
        if continue_message:
            with open(FILE_PATH, "a") as file:
                file.write(f"{website_entry.get().strip()} | {email_entry.get().strip()} | {password_input.get().strip()}\n")
            messagebox.showinfo("Saved", "Password saved successfully")
            
        email_entry.delete(0, "end")
        password_input.delete(0, "end")
        website_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #
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
email_entry.insert(0, "@gmail.com")
email_entry.grid(row=2, column=1, pady=5, padx=5, ipady=2, columnspan=2, sticky="ew")

# password label and field
password_label = Label(text="Password")
password_label.grid(row=3, column=0)
# Entry
password_input = Entry()
password_input.grid(row=3, column=1, padx=5, pady=5, ipady=2, sticky="ew")
# Btn
password_gen_btn = Button(text="Generate Password", command=password_generator)
password_gen_btn.grid(row=3, column=2, padx=5, ipadx=2, sticky="ew")


# Add password btn
add_btn = Button(text="Add", command=add_password)
add_btn.grid(row=4, column=1, padx=5, pady=5, columnspan=2, sticky="ew")

window.mainloop()