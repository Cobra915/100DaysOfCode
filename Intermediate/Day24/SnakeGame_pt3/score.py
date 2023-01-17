from turtle import Turtle

ALIGNMENT = 'center'
FONT = 'Arial'
FONT_SIZE = 20

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.read_local()
        self.goto(0, 270)
        self.hideturtle()
        self.pencolor('white')
        self.scribble()

    def add_point(self):
        self.score += 1
        self.clear()
        self.scribble()

    def scribble(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.highscore}', False, align=ALIGNMENT, font=(FONT, FONT_SIZE, 'normal'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.write_local()
        self.score = 0
        self.scribble()

    def read_local(self):
        with open('./SnakeGame_pt3/highscore.txt') as file:
            contents = file.read()
            self.highscore = int(contents)

    def write_local(self):
        with open('./SnakeGame_pt3/highscore.txt', mode='w') as file:
            file.write(str(self.highscore))

    # def game_over(self):
        # self.clear()
        # self.write(f'Game over, your final score is: {self.score} ', False, align=ALIGNMENT, font=(FONT, FONT_SIZE, 'normal'))
        