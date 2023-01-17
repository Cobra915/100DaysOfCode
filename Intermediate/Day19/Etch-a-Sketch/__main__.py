if __name__ == '__main__':
    from turtle import Turtle, Screen

    timmy = Turtle()
    screen = Screen()

    def move_forwards():
        timmy.forward(10)

    def turn_right():
        timmy.right(10)

    def turn_left():
        timmy.left(10)

    def move_back():
        timmy.backward(10)

    def clear_canvas():
        timmy.reset()

    screen.listen()
    screen.onkey(key='w', fun=move_forwards)
    screen.onkey(key='d', fun=turn_right)
    screen.onkey(key='a', fun=turn_left)
    screen.onkey(key='s', fun=move_back)
    screen.onkey(key='c', fun=clear_canvas)

    screen.exitonclick()