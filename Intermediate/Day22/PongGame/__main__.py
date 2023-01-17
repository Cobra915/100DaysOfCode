if __name__ == '__main__':
    from turtle import Screen
    from paddle import Paddle
    import time
    from ball import Ball
    from score import Score, Court

    mypaddle = Paddle()
    mypaddle.setx(350)
    opppaddle = Paddle()
    opppaddle.setx(-350)
    ball = Ball()
    score = Score()
    court = Court()

    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor('black')
    screen.title('Pong')
    screen.tracer(0)
    screen.listen()
    screen.onkeypress(key='Up', fun=mypaddle.move_up)
    screen.onkeypress(key='Down', fun=mypaddle.move_down)

    screen.onkeypress(key='w', fun=opppaddle.move_up)
    screen.onkeypress(key='s', fun=opppaddle.move_down)

    game_on = True
    while game_on:

        screen.update()
        time.sleep(0.1)
        ball.move()
        # detect ball colliding with r_paddle, invoke bounce
        if ball.xcor() >= 330 and ball.distance(mypaddle) <= 50:
            ball.bounce_x()
        # detect ball colliding with l_paddle, invoke bounce
        if ball.xcor() >= -340 and ball.distance(opppaddle) <= 50:
            ball.bounce_x()
        # detect ball colliding with top, invoke bounce
        if ball.ycor() > 280 or ball.ycor() < -270:
            ball.bounce_y()
        # detect ball colliding with right wall, invoke add_point, reset
        if ball.xcor() >= 380:
            score.point_opponent()
            ball.reset()
            mypaddle.sety(0)
            opppaddle.sety(0)
            time.sleep(2)
        # detect ball colliding with left wall, invoke add_point, reset
        if ball.xcor() <= -390:
            score.point_player()
            ball.reset()
            mypaddle.sety(0)
            opppaddle.sety(0)
            time.sleep(2)





    screen.exitonclick()