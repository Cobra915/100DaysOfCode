if __name__=='__main__':
    import tkinter

    def button_clicked():
        result.config(text=f'{round(float(mile_input.get())*1.609344)}')

    window = tkinter.Tk()
    window.title('Mile to Km Converter')
    window.config(padx=20, pady=20)

    # Labels
    Miles = tkinter.Label(text='Miles')
    Miles.grid(column=2, row=0)

    equal_to = tkinter.Label(text='is equla to')
    equal_to.grid(column=0, row=1)

    km = tkinter.Label(text='Km')
    km.grid(column=2, row=1)

    result = tkinter.Label(text='')
    result.grid(column=1, row=1)

    # Button
    button = tkinter.Button(text='Calculate', command=button_clicked)
    button.grid(column=1, row=2)

    # Entry
    mile_input = tkinter.Entry(width=10)
    mile_input.insert(tkinter.END, string='0')
    mile_input.grid(column=1, row=0)

    window.mainloop()