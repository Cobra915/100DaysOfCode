from tkinter import *
from tkinter import messagebox
import json
import random
import string
import pyperclip

LETTER_LENGTH = 8
SYMBOL_LENGTH = 4
NUMBER_LENGTH = 4
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pw():
    letter_choices = string.ascii_letters
    symbol_choices = string.punctuation
    number_choices = string.digits

    lett = [random.choice(letter_choices) for letter in range(LETTER_LENGTH)]
    sym = [random.choice(symbol_choices) for _ in range(SYMBOL_LENGTH)]
    num = [random.choice(number_choices) for _ in range(NUMBER_LENGTH)]

    pw_final = lett + sym + num

    random.shuffle(pw_final)

    pw_final = ''.join(pw_final)
    password_entry.delete(0, END)
    password_entry.insert(END, string=pw_final)    
    pyperclip.copy(pw_final)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pw():        
    website = website_entry.get().lower()
    email_username = email_username_entry.get()
    password = password_entry.get()
    
    if len(website) == 0 or len(password) == 0 or len(email_username) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")

    else:
        new_data = {
            website : {
                'email' : email_username, 
                'password' : password
            } 
        }                
    
        try:
            with open('./PasswordManagerRevisited/passwords.json', mode='r') as fin:
                if fin.read() == '':
                    raise FileNotFoundError
                fin.seek(0)
                DictObj = json.load(fin)

        except FileNotFoundError:
            print('local files not present, creating files...')
            DictObj = {}
            DictObj.update(new_data)
            with open('./PasswordManagerRevisited/passwords.json', mode='w') as fin:
                json.dump(DictObj, fin, indent=4, separators=(',',': '))
            print('successfully created files...')

        else:
            DictObj.update(new_data)

            with open('./PasswordManagerRevisited/passwords.json', mode='w') as fin:
                json.dump(DictObj, fin, indent=4, separators=(',',': '))
                print('successfully appended credentials to the JSON file')

        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            email_username_entry.delete(0, END)


def search_pw():
    try:
        with open(f'./PasswordManagerRevisited/passwords.json', mode='r') as fin:
            if fin.read() == '':
                raise FileNotFoundError
            fin.seek(0)
            data = json.load(fin)

    except FileNotFoundError:
        messagebox.showinfo(title='File not found', message='File not found or is empty')

    else:
        list = [value for key, value in data.items() if website_entry.get().lower() in key.lower()]
        if len(list)>0:
            message = ''
            for num in range(len(list)):
                message += f'Entry #{num+1}:\n{list[num]}\n'
            messagebox.showinfo(title=f'{len(list)} credential(s) found: ', message=message)
        else:
            messagebox.showinfo(title="No match found", message=f'No credential match for substring: {website_entry.get()}')


# ---------------------------- UI SETUP ------------------------------- #

if __name__ == '__main__':
    window = Tk()
    window.title('Password Manager')
    window.config(padx=20, pady=20)

    canvas = Canvas(width=200, height=200)
    logo_image = PhotoImage(file='./PasswordManagerRevisited/logo.png')
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
    website_entry = Entry(width=32)
    #Add some text to begin with
    website_entry.grid(column=1, row=1, columnspan=2, sticky=W)


    email_username_entry = Entry(width=32)
    #Add some text to begin with
    email_username_entry.grid(column=1, row=2, columnspan=2, sticky=W)

    password_entry = Entry(width=32)
    password_entry.grid(column=1, row=3, sticky=W)
    #Add some text to begin with
    

    # Buttons
    generate_button = Button(text='Generate Password', command=generate_pw)
    generate_button.grid(column=2, row=3, sticky=W)

    add_button = Button(text='Add', command=add_pw, width=44)
    add_button.grid(column=1, row=4, columnspan=2, sticky=W)

    search_button = Button(text='Search', command=search_pw)
    search_button.grid(column=2, row=1, sticky=W)

    window.mainloop()