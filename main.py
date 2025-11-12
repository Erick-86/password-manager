# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)
window.resizable(False, False)

# Logo 
canvas = Canvas(width=150, height=170, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(60, 120, image=img)
canvas.grid(row=0, column=0, columnspan=2)

window.mainloop()