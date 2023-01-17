BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = 'Ariel'
correct_count = 0
incorrect_count = 0
word = ''
words_left = 0
COUNTDOWN_TIMER = 5
timer = None
data_dict = {}

from tkinter import *
from tkinter import messagebox
import pandas
import random
from CustomMessagebox import LanguageSelect, func

# Functions/Classes

class DeckCompleteError(Exception):
    #Raised when the flash card deck is complete
    pass

def start_timer():
        countdown(COUNTDOWN_TIMER)

def countdown(count):
    global timer
    if count >= 0:
        Timer.config(text=f'{count}')
        timer = window.after(1000, countdown, count-1)
    else:
        reveal_word()

def correct():
    global correct_count
    global data_dict
    correct_count += 1
    data_dict.remove(word)
    data_dict = update_local(data_dict)
    Correct.config(text=f'Correct: {correct_count}')
    
    new_word()

def incorrect():
    global incorrect_count
    incorrect_count += 1
    Incorrect.config(text=f"Incorrect: {incorrect_count}")
    new_word()

def new_word():
    global word
    word = random.choice(data_dict)
    Words_Left.config(text=f'{len(data_dict)} words remaining')
    canvas.itemconfig(canvas_image, image=cardf_image)
    canvas.itemconfig(language_text, text=language, fill='black')
    canvas.itemconfig(word_text, text=word[language], fill='black')
    start_timer()

def update_local(data_dict:list):
    if len(data_dict)>0:
        df = pandas.DataFrame(data_dict)
        df.to_csv(SAVE_FILEPATH, index=False)
    else:
        df = pandas.DataFrame(data_dict)
        df.to_csv(SAVE_FILEPATH)
        data_dict = read_local()
    return data_dict

def read_local():
    try:
        data = pandas.read_csv(SAVE_FILEPATH)
        data_dict = data.to_dict(orient='records')
        # Ensure file has not been emptied by pandas write
        if len(data_dict) == 0:
            raise DeckCompleteError

    except FileNotFoundError:
        print('local save files either not present or empty, opening new session')
        messagebox.showinfo(title='File not found', message='File not found, creating new deck from original list')
        data = pandas.read_csv(NEW_FILEPATH)
        data_dict = data.to_dict(orient='records')

    except DeckCompleteError:
        is_ok = messagebox.askokcancel(title='Restart?', message='You\'ve completed your deck of flashcards!\n\nClick \'Ok\' to restart with the original deck.\nClick \'Cancel\' to quit.')

        if is_ok:
            data = pandas.read_csv(NEW_FILEPATH)
            data_dict = data.to_dict(orient='records')
        else:
            exit()

    return data_dict

def reveal_word():
    global word
    canvas.itemconfig(canvas_image, image=cardb_image)
    canvas.itemconfig(language_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=word['English'], fill='white')

# main
if __name__ == '__main__':

    # UI Setup
    window = Tk()
    window.title('Flash Card App')
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
    check_image = PhotoImage(file='./FlashCardApp/images/right.png')
    wrong_image = PhotoImage(file='./FlashCardApp/images/wrong.png')
    cardf_image = PhotoImage(file='./FlashCardApp/images/card_front.png')
    cardb_image = PhotoImage(file='./FlashCardApp/images/card_back.png')

    canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
    canvas_image = canvas.create_image(400,263 , image=cardf_image)
    language_text = canvas.create_text(400, 150, text = 'In the accompanying popup', fill='black', font=(FONT_NAME, 40, 'italic'))
    word_text = canvas.create_text(400, 263, text = 'Select a language', fill ='black', font=(FONT_NAME, 60, 'italic'))
    canvas.grid(column=0, row=0, columnspan=2)

    ## Labels
    Correct = Label(text=f'Correct: {correct_count}', bg=BACKGROUND_COLOR, font=(FONT_NAME, 20, 'bold'))
    Correct.grid(column=1, row=2)
    Incorrect = Label(text=f'Incorrect: {incorrect_count}', bg=BACKGROUND_COLOR, font=(FONT_NAME, 20, 'bold'))
    Incorrect.grid(column=0, row=2)

    Timer = Label(text='timer', bg=BACKGROUND_COLOR, font=(FONT_NAME, 30, 'bold'))
    Timer.grid(column=0, row=3, columnspan=2)

    Words_Left = Label(text=f'{len(data_dict)} words remaining', bg=BACKGROUND_COLOR, font=(FONT_NAME, 20, 'bold'))
    Words_Left.grid(column=0, row=4, columnspan=2)

    ## Buttons
    check_button = Button(image = check_image, command=correct)
    check_button.grid(column=1, row=1)

    wrong_button = Button(image= wrong_image, command=incorrect)
    wrong_button.grid(column=0, row=1)

    language = func()

    BACKGROUND_COLOR = "#B1DDC6"
    FONT_NAME = 'Ariel'
    NEW_FILEPATH = f'./FlashCardApp/data/{language}_words.csv'
    SAVE_FILEPATH = f'./FlashCardApp/data/{language}_words_to_learn.csv'

    # Load data
    data_dict = read_local()

    new_word()

    window.mainloop()