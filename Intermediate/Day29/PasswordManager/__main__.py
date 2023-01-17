from tkinter import *
from tkinter import messagebox
import os
import random
import string
import pyperclip

LETTER_LENGTH = 8
SYMBOL_LENGTH = 4
NUMBER_LENGTH = 4

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pw():
    pw = []

    pw = generate_letters(LETTER_LENGTH, pw)
    pw = generate_symbols(SYMBOL_LENGTH, pw)
    pw = generate_numbers(NUMBER_LENGTH, pw)

    pw_final = ''.join(pw)
    password_entry.delete(0, END)
    password_entry.insert(END, string=pw_final)
    pyperclip.copy(pw_final)



def generate_letters(letter_length, pw):
    letter_choices = string.ascii_letters
    for letter in range(letter_length):
        letter = random.choice(letter_choices)
        pw.append(letter)
    return pw

def generate_symbols(symbol_length, pw):
    symbol_choices = string.punctuation
    for symbol in range(symbol_length):
        pw.insert(random.randint(0, len(pw)), random.choice(symbol_choices))
    return pw

def generate_numbers(number_length, pw):
    number_choices = string.digits
    for number in range(number_length):
        pw.insert(random.randint(0, len(pw)), random.choice(number_choices))
    return pw


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pw():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0 or len(email_username) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")

    else:
        is_ok = messagebox.askokcancel(title=website, message=
        f"These are the details entered: \nEmail: {email_username} "
        f"\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open(f'./PasswordManager/passwords.txt', mode='a') as fin:
                fin.write(f'{website} | {email_username} | {password} \n')
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                email_username_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

if __name__ == '__main__':
    window = Tk()
    window.title('Password Manager')
    window.config(padx=20, pady=20)

    canvas = Canvas(width=200, height=200)
    logo_image = PhotoImage(file='./PasswordManager/logo.png')
    canvas.create_image(100, 100, image=logo_image)
    canvas.grid(column=1, row=0)


    # Labels
    website_label = Label(text="Website:")
    website_label.grid(column=0, row=1)

    email_username_label = Label(text='Email/Username:')
    email_username_label.grid(column=0, row=2)

    password_label = Label(text='Password:')
    password_label.grid(column=0, row=3)

    #Entries
    website_entry = Entry(width=52)
    #Add some text to begin with
    website_entry.grid(column=1, row=1, columnspan=2, sticky=W)


    email_username_entry = Entry(width=52)
    #Add some text to begin with
    email_username_entry.grid(column=1, row=2, columnspan=2, sticky=W)

    password_entry = Entry(width=21)
    password_entry.grid(column=1, row=3, sticky=W)
    #Add some text to begin with
    

    # Buttons
    generate_button = Button(text='Generate Password', command=generate_pw)
    generate_button.grid(column=2, row=3, sticky=W)

    add_button = Button(text='Add', command=add_pw, width=44)
    add_button.grid(column=1, row=4, columnspan=2, sticky=W)

    window.mainloop()