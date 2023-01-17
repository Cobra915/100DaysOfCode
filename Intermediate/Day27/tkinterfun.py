import tkinter
import turtle

def button_clicked():
    button_label = tkinter.Label(text='I got clicked!')
    button_label.grid(column=1, row=2)
    my_label.config(text=input.get())

window = tkinter.Tk()
window.title('My first GUI program')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text='I am a Label', font=("Arial", 24, "bold"))
my_label.config(text='New Text')
my_label.grid(column=0, row=0)

# Button
button = tkinter.Button(text='Click Me', command=button_clicked)
button.grid(column=1, row=1)

# Entry
input = tkinter.Entry(width=30)
input.insert(tkinter.END, string='I want to feel words inside me')
input.grid(column=3, row=2)

# New Button
button = tkinter.Button(text='No, Click Me', command=button_clicked)
button.grid(column=2, row=0)

window.mainloop()