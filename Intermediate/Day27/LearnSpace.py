# Tkinter, *args, **kwargs and Creating GUI Programs

import tkinter
import turtle

window = tkinter.Tk()
window.title('My first GUI program')
window.minsize(width=500, height=300)


my_label = tkinter.Label(text='I am a Label', font=("Arial", 24, "bold"))
my_label.pack()

my_label['text'] = 'New Text'
my_label.config(text='New Text')

# Button
def button_clicked():
    button_label = tkinter.Label(text='I got clicked!')
    button_label.pack()
    my_label.config(text=input.get())

button = tkinter.Button(text='Click Me', command=button_clicked)
button.pack()

# Entry

input = tkinter.Entry(width=10)
input.pack()
input.get()

# tim = turtle.Turtle()
#tim.write()

#Notice how the write functions of turtel has more description than pack from tkinter. notice the **kw on the hover discover of pack

# Default Arguments

# def print(a, b=4, c=9):
#     return (a, b, c)

# Unless you feed the method 2 or three values, be and c will always be 4 and 9 respectively.

# Advanced Python Arguments
# def add(n1, n2):
#     sum = n1 + n2
#     return sum

    # obvi add(n1=5, n2=3) will return 8
    # what if you wanted to have more thand two? What if you wanted to have infinite? Enter *args

# def add(*args):
#     input_sum = 0
#     for n in args:
#         input_sum += n
#     # or
#     # input_sum = sum(args)
#     return input_sum



# sum = add(5, 23, 6, 4, 34, 3, 45, 56, 6, 4, 3, 4, 5, 5, 4, 3, 2, 2, 21, 23, 3, 34)
# print(f'The sum is {sum}')

# So it's nice that we can refer to our arguments because they're a tuple, we can use ppositional statements, (i.e. args[1] = 23 from above). But what if we wanted to refer to them by name, rather than position?
# Enter **kwargs

# def calculate(n, **kwargs):
#     print(kwargs) #prints a dict
#     # You could loop through them like below
#     for key, value in kwargs:
#         print(key)
#         print(value)

#     # or you could simply call them by name
    
#     print['add']

#     # What this allows us to do is to accept arguments with keywordds, and do stuff if and only if they're entered, say we take in a required arg as the subject. We'll call it n

#     n += kwargs['add']
#     n -= kwargs['subtract']
#     n *= kwargs['multiply']
#     n /= kwargs['divide']
#     return n

# result = calculate(4, add=3, subtract=5, multiply=5, divide=2)
# print(result)

# notice how above if you didn't pass any of the 4 into the function, it'd error out, this is where the dict method get() comes into play

# class Car:
#     def __init__(self, **kw):
#         self.make = kw.get('make')
#         self.model = kw.get('model')
#         self.color = kw.get('color')
#         self.seats = kw.get('seats')

# my_car = Car(make='Ford', make='Focus ST', color='Race Red', seats=5)

# Now that we're using get, if you don't specify any args, the value retrieved by the get will simply be a None

window.mainloop()

