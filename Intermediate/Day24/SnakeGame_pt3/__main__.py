if __name__ == '__main__':
    from turtle import Screen
    from snake import Snake
    import time
    from food import Food
    from score import Score

    snek = Snake()
    fewd = Food()
    score = Score()

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


    while True:
        screen.update()
        time.sleep(0.1)
        snek.move_forwards()

        # Detecting collision with food
        if snek.head.distance(fewd) < 15:
            snek.add_seg()
            fewd.refresh()
            score.add_point()
        
        # Detecting collision with self
        for segment in snek.turts[1:]:
            if snek.head.distance(segment) < 10:
                score.reset()
                snek.reset()

        # Detecting collision with wall
        if snek.head.xcor() >= 300 or snek.head.xcor() <= -300 or snek.head.ycor() >= 300 or snek.head.ycor() <= -300:
            score.reset()
            snek.reset()


    screen.exitonclick()