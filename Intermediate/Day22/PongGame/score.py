from turtle import Turtle

ALIGNMENT = 'center'
FONT = 'Arial'
FONT_SIZE = 20

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.myscore = 0
        self.oppscore = 0
        self.hideturtle()
        self.pencolor('white')
        self.penup()
        self.scribble()

    def point_player(self):
        self.myscore += 1
        self.clear()
        self.scribble()
    
    def point_opponent(self):
        self.oppscore += 1
        self.clear()
        self.scribble()

    def scribble(self):
        self.clear()
        self.goto(0, 270)
        self.write(f'Score:', False, align=ALIGNMENT, font=(FONT, FONT_SIZE, 'normal'))
        self.goto(0, 240)
        self.write(f'{self.myscore}     {self.oppscore}', False, align=ALIGNMENT, font=(FONT, FONT_SIZE, 'normal'))

    def game_over(self):
        self.clear()
        self.goto(0, 270)
        self.write(f'Score:', False, align=ALIGNMENT, font=(FONT, FONT_SIZE, 'normal'))
        self.goto(0, 240)
        self.write(f'{self.myscore}     {self.oppscore}', False, align=ALIGNMENT, font=(FONT, FONT_SIZE, 'normal'))


class Court(Turtle):
    def __init__(self):
        super().__init__()
        self.myscore = 0
        self.oppscore = 0
        self.color('white')
        self.hideturtle()
        self.pencolor('white')
        self.penup()
        self.draw_dotted()
    def draw_dotted(self):
        self.goto(0,-300)
        self.setheading(90)
        while self.ycor() < 300:
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
        self.penup()