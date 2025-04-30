from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
from click import command

FONT_NAME = 'Courier'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()

    data = f"{website} | {email} | {password}\n"

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops!", message="Please Fill in All fields.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Your Details are:\n Email: {email}\n password: {password}\n Is this Right?")

        if is_ok:
            with open('data.txt', 'a') as file:
                file.write(data)

            website_entry.delete(0, 'end')
            username_entry.delete(0, 'end')
            password_entry.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(width=400, height=400, padx=100, pady=50)

canvas = Canvas(width=200, height=200, bg='Black')
password_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=password_image)
canvas.grid(row=0, column=1)


website_label = Label(text='Website:', font=(FONT_NAME, 10, 'bold'))
website_label.grid(row=1, column=0)

website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2)

username_label = Label(text='Email/Username:', font=(FONT_NAME, 10, 'bold'))
username_label.grid(row=2, column=0)

username_entry = Entry(width=40)
username_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text='Password:', font=(FONT_NAME, 10, 'bold'))
password_label.grid(row=3, column=0)

password_entry = Entry(width=40)
password_entry.grid(row=3, column=1, columnspan=2)

generate_button = Button(text='Generate Password', command=generate_password)
generate_button.grid(row=3, column=2)
#
add_button = Button(text='Add', width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()