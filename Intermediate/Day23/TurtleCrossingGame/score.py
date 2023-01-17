from turtle import Turtle

ALIGNMENT = 'center'
FONT = 'Arial'
FONT_SIZE = 20

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.mylevel = 0
        self.hideturtle()
        self.pencolor('white')
        self.penup()
        self.scribble()

    def next_level(self):
        self.mylevel += 1
        self.clear()
        self.scribble()

    def scribble(self):
        self.clear()
        self.goto(0, 270)
        self.write(f'Score:', False, align=ALIGNMENT, font=(FONT, FONT_SIZE, 'normal'))
        self.goto(0, 240)
        self.write(f'Level : {self.mylevel}', False, align=ALIGNMENT, font=(FONT, FONT_SIZE, 'normal'))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f'GAME OVER', False, align=ALIGNMENT, font=(FONT, FONT_SIZE, 'normal'))