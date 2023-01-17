import tkinter

expression = ''

def press(num):
    global expression

    expression = expression + str(num)
    result.set(expression)

def equal_press():
    try:
    
        global expression

        total = str(eval(expression))
        expression = total
        result.set(total)

    except:
        result.set(' error ')
        expression = ''

def clear_press():
    global expression

    expression = ''
    result.set(expression)

def neg_pos_press():
    global expression

    if expression[0] == '-':
        expression = expression.replace('-', '')
        result.set(expression)

    else:
        expression = '-' + expression
        result.set(expression)

def percent_press():
    global expression

    expression =  str(float(expression)/100)
    result.set(expression)

if __name__=='__main__':

    window = tkinter.Tk()
    window.title('Calculator')
    window.config(padx=40, pady=40)

    result = tkinter.StringVar()

    # Function Buttons
    add_button = tkinter.Button(text='+', font=(10),  width=5, height=3, command=lambda: press('+'))
    add_button.grid(column=3, row=4)

    subtract_button = tkinter.Button(text='-', font=(10), width=5, height=3, command=lambda: press('-'))
    subtract_button.grid(column=3, row=3)

    multiply_button = tkinter.Button(text='x', font=(10), width=5, height=3, command=lambda: press('*'))
    multiply_button.grid(column=3, row=2)

    divide_button = tkinter.Button(text='/', font=(10), width=5, height=3, command=lambda: press('/'))
    divide_button.grid(column=3, row=1)

    equal_button = tkinter.Button(text='=', font=(10), width=5, height=3, command=lambda: equal_press())
    equal_button.grid(column=3, row=5)

    clear_button = tkinter.Button(text='C', font=(10), width=5, height=3, command=lambda: clear_press())
    clear_button.grid(column=0, row=1)

    neg_pos_button = tkinter.Button(text='(-)', font=(10), width=5, height=3, command=lambda: neg_pos_press())
    neg_pos_button.grid(column=1, row=1)

    percent_button = tkinter.Button(text='%', font=(10), width=5, height=3, command=lambda: percent_press())
    percent_button.grid(column=2, row=1)

    # Number Buttons
    one_button = tkinter.Button(text='1', font=(10), width=5, height=3, command=lambda: press(1))
    one_button.grid(column=0, row=4)

    two_button = tkinter.Button(text='2', font=(10), width=5, height=3, command=lambda: press(2))
    two_button.grid(column=1, row=4)

    three_button = tkinter.Button(text='3', font=(10), width=5, height=3, command=lambda: press(3))
    three_button.grid(column=2, row=4)

    four_button = tkinter.Button(text='4', font=(10), width=5, height=3, command=lambda: press(4))
    four_button.grid(column=0, row=3)

    five_button = tkinter.Button(text='5', font=(10), width=5, height=3, command=lambda: press(5))
    five_button.grid(column=1, row=3)

    six_button = tkinter.Button(text='6', font=(10), width=5, height=3, command=lambda: press(6))
    six_button.grid(column=2, row=3)

    seven_button = tkinter.Button(text='7', font=(10), width=5, height=3, command=lambda: press(7))
    seven_button.grid(column=0, row=2)

    eight_button = tkinter.Button(text='8', font=(10), width=5, height=3, command=lambda: press(8))
    eight_button.grid(column=1, row=2)

    nine_button = tkinter.Button(text='9', font=(10), width=5, height=3, command=lambda: press(9))
    nine_button.grid(column=2, row=2)

    zero_button = tkinter.Button(text='0', font=(10), height =3, command=lambda: press(0))
    zero_button.grid(column=0, row=5, columnspan = 2, sticky = tkinter.W+tkinter.E)

    period_button = tkinter.Button(text='.', font=(10), width=5, height=3, command=lambda: press('.'))
    period_button.grid(column=2, row=5)    

    # Entry
    result_field = tkinter.Entry(window, textvariable=result, font=(10))
    result_field.grid(column=0, row=0, columnspan = 4, sticky = tkinter.W+tkinter.E)

    window.mainloop()