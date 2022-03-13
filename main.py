from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- GENERATE PASSWORD ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # reset password entry in case user pressed generate without saving previous generation
    password_entry.delete(0, END)

    password_letters = [random.choice(letters) for _ in range(letters_slider.get())]
    password_numbers = [random.choice(numbers) for _ in range(numbers_slider.get())]
    password_symbols = [random.choice(symbols) for _ in range(symbols_slider.get())]

    password_list = password_numbers + password_symbols + password_letters
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

    # copy generated password to clipboard, so user can paste into browser right away
    pyperclip.copy(password)

# ---------------------------- SET SLIDERS TO DEFAULT VALUES ------------------------------- #
def set_sliders():
    default_letters = 8
    default_numbers = 4
    default_symbols = 2
    letters_slider.set(default_letters)
    numbers_slider.set(default_numbers)
    symbols_slider.set(default_symbols)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Details entered: \nemail: {email}"
                                                      f"\npassword: {password} \nDo you want to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

            set_sliders()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

total_letters_label = Label(text="Total letters:")
total_letters_label.grid(row=5, column=0)

total_numbers_label = Label(text="Total numbers:")
total_numbers_label.grid(row=6, column=0)

total_symbols_label = Label(text="Total symbols:")
total_symbols_label.grid(row=7, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "wendyyuxuanzhang@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

# Sliders
letters_slider = Scale(window, from_=0, to=16, orient=HORIZONTAL)
letters_slider.grid(row=5, column=1)

numbers_slider = Scale(window, from_=0, to=16, orient=HORIZONTAL)
numbers_slider.grid(row=6, column=1)

symbols_slider = Scale(window, from_=0, to=16, orient=HORIZONTAL)
symbols_slider.grid(row=7, column=1)

set_sliders()


window.mainloop()
