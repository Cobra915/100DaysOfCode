from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = '#375362'

class QuizInterface:
    def __init__(self, quiz_brain : QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            text='test', 
            fill=THEME_COLOR, 
            width=280, 
            font=("Arial", 20, "italic")
            )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        

        # Buttons
        true_img = PhotoImage(file='./QuizGame/images/true.png')
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.answer_true)
        self.true_button.grid(column=0, row=2)

        false_img = PhotoImage(file='./QuizGame/images/false.png')
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.answer_false)
        self.false_button.grid(column=1, row=2)

        # Labels
        self.score_label = Label(text=f'Score: 0', bg=THEME_COLOR, fg='white')
        self.score_label.grid(row=0, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
        else:
            self.score_label.config(text=f'Score: {self.quiz.score}')
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def answer_true(self):
        is_right = self.quiz.evaluate_answer('True')
        self.give_feedback(is_right)



    def answer_false(self):
        is_right = self.quiz.evaluate_answer('False')
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)

        