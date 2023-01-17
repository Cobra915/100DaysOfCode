if __name__ == '__main__':
    from turtle import Turtle, Screen
    import random

    color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

    screen = Screen()
    screen.setup(width=1250, height=800)
    screen.title('Welcome to my turt race!')
    bet = screen.textinput('Bet', f"Which turt do you think will win? {'/'.join(color_list)}: ")
    while bet not in color_list:
        bet = screen.textinput('Bet Error', f"Please enter a valid selection. Which turt do you think will win? {'/'.join(color_list)}: ")

    trtls = [Turtle() for i in range((len(color_list)))]
    racers = len(color_list)
    pos_inc = 400/racers
    pos = -pos_inc*(racers/2)
    i = 0
    racers = len(color_list)
    for trtl in trtls:
        trtl.color(color_list[i])
        trtl.shape('turtle')
        trtl.penup()
        trtl.setpos(-615, pos)
        pos += pos_inc
        i+=1

    is_winner = False
    while not is_winner:
        for trtl in trtls:
            trtl.forward(random.randint(0,5))
            if trtl.xcor() >= 600:
                winner = trtl.color()[0]
                is_winner = True

    print('It\'s over! That took forever...')

    if winner == bet:
        print(f'You win! The winner is {winner.title()}!')
    else:
        print(f'You lose! The winner is {winner.title()}!')

    #screen = Screen()
    screen.exitonclick()