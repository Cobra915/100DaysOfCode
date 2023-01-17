from tkinter import *
import urllib3
import json


def get_quote():
    http = urllib3.PoolManager()
    req = http.request('GET',"https://api.kanye.rest")
    print(req.status)
    response = req.data
    string = response.decode('utf8')
    data = json.loads(string)
    quote = data['quote']
    canvas.itemconfig(quote_text, text = quote)

if __name__ == '__main__':
    window = Tk()
    window.title("Kanye Says...")
    window.config(padx=50, pady=50)

    canvas = Canvas(width=300, height=414)
    background_img = PhotoImage(file="./KanyeQuotesApp/background.png")
    canvas.create_image(150, 207, image=background_img)
    quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 24, "bold"), fill="white")
    canvas.grid(row=0, column=0)

    kanye_img = PhotoImage(file="./KanyeQuotesApp/kanye.png")
    kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
    kanye_button.grid(row=1, column=0)

    window.mainloop()