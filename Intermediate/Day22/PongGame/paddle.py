from turtle import Turtle

MOVE_DISTANCE = 40
PADDLE_SIZE = 4
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        new_ypos = self.ycor() + MOVE_DISTANCE
        self.goto((self.xcor(), new_ypos))

    def move_down(self):
        new_ypos = self.ycor() - MOVE_DISTANCE
        self.goto((self.xcor(), new_ypos))