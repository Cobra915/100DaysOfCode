from turtle import Turtle

MOVE_SPEED = 10

class MyTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color('green')
        self.setheading(90)
        self.go_to_start()


    def move_up(self):
        new_y = self.ycor() + MOVE_SPEED
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - MOVE_SPEED
        self.goto(self.xcor(), new_y)

    def move_left(self):
        new_x = self.xcor() - MOVE_SPEED
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + MOVE_SPEED
        self.goto(new_x, self.ycor())

    def go_to_start(self):
        self.setpos(0, -280)