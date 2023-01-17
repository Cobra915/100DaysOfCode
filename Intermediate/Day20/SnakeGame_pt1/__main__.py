if __name__ == '__main__':
    from turtle import Screen
    from snake import Snake
    import time

    snek = Snake()

    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title('Welcome to my Snake Game!')
    screen.tracer(0)
    screen.listen()
    screen.onkey(key='Up', fun=snek.up)
    screen.onkey(key='Down', fun=snek.down)
    screen.onkey(key='Left', fun=snek.left)
    screen.onkey(key='Right', fun=snek.right)

    is_dead = False
    while not is_dead:
        screen.update()
        time.sleep(0.1)
        snek.move_forwards()

    screen.exitonclick()