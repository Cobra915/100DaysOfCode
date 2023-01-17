from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_LENGTH = 3
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        self.create_snake()
        self.head = self.turts[0]

    def create_snake(self):
        self.turts = [Turtle() for i in range(0,STARTING_LENGTH)]
        pos = 0

        for turt in self.turts:
            turt.penup()
            turt.color('white')
            turt.shape('square')
            turt.setx(pos)
            pos -= 20

    def add_seg(self):
        pos = self.turts[-1].pos()
        self.turts.append(Turtle())
        new_seg = self.turts[-1]
        new_seg.penup()
        new_seg.color('white')
        new_seg.shape('square')
        new_seg.goto(pos)

    def move_forwards(self):
        positions = []
        positions.append(self.head.pos())
        self.head.forward(MOVE_DISTANCE)
        for turt in range(1,len(self.turts)):
            positions.append(self.turts[turt].pos())
            self.turts[turt].goto(positions[turt-1])

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)