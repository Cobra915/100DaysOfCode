from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global checks
    global reps
    global timer

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f'00:00')
    Timer.config(text="Timer", fg=GREEN)
    checks = ''
    result_field.config(text=checks)
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    global checks
    reps += 1

    if reps % 8 == 0:
        Timer.config(text="Break", fg=RED)
        reps = 0
        checks = ''
        result_field.config(text=checks)
        countdown(LONG_BREAK_MIN*60)
    elif reps % 2 == 0:
        Timer.config(text="Break", fg=PINK)
        checks += '✔'
        result_field.config(text=checks)
        countdown(SHORT_BREAK_MIN*60)
    else:
        Timer.config(text="Work", fg=GREEN)
        countdown(WORK_MIN*60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global timer
    if count >= 0:
        count_min = math.floor(count/60)
        count_sec = count%60
        if count_sec < 10:
            count_sec = '0' + str(count_sec)
        canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
        timer = window.after(1000, countdown, count-1)
    else:
        raise_above_all(window)
        start_timer()

def raise_above_all(window):
    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file='./PomodoroApp/tomato.png')
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text = '00:00', fill='white', font=(FONT_NAME, 30, 'bold'))
canvas.grid(column=1, row=1)

# Labels
Timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, 'bold'))
Timer.grid(column=1, row=0)

checks = ''

result_field = Label(window, text=f'{checks}', fg=GREEN, bg=YELLOW, font=(10))
result_field.grid(column=1, row=3)

# Buttons
start_button = Button(text='Start', font=(10), width=5, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', font=(10), width=5, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()