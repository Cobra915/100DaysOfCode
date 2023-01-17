from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.speed('fastest')
        self.setheading(35)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1
        self.x_move *= 1.2
        self.y_move *= 1.2

    def bounce_y(self):
        self.y_move *= -1

    def reset(self):
        self.x_move = 10
        self.y_move = 10
        self.setpos(0,0)
        num = [-1,1][random.randrange(2)]
        self.y_move *= num
        self.x_move *= num
