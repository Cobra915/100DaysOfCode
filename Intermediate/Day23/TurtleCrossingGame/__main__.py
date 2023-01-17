if __name__ == '__main__':
    from turtle import Screen
    from myturtle import MyTurtle
    import time
    from car import CarManager
    from score import Score

    myturtle = MyTurtle()
    score = Score()
    carmanager = CarManager()

    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor('black')
    screen.title('Pong')
    screen.tracer(0)
    screen.listen()
    screen.onkeypress(key='Up', fun=myturtle.move_up)
    screen.onkeypress(key='Down', fun=myturtle.move_down)
    screen.onkeypress(key='Left', fun=myturtle.move_left)
    screen.onkeypress(key='Right', fun=myturtle.move_right)

    game_on = True
    while game_on:
        time.sleep(0.1)
        screen.update()

        carmanager.create_car()
        carmanager.move_cars()

        # detect car colliding with turtle
        for car in carmanager.all_cars:
            if car.distance(myturtle) < 20:
                score.game_over()
                game_on = False

        # detect player presence at finish line
        if myturtle.ycor() >= 280:
            myturtle.go_to_start()
            score.next_level()
            carmanager.next_level()

    screen.exitonclick()