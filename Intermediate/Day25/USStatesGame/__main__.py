if __name__ == '__main__':

    import turtle
    import pandas

    FONT = 'Arial'
    FONT_SIZE = 20

    data = pandas.read_csv('./USStatesGame/50_states.csv')

    screen = turtle.Screen()
    screen.title("U.S. States Game")
    image = './USStatesGame/blank_states_img.gif'
    screen.addshape(image)
    turtle.shape(image)

    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()

    score_writer = turtle.Turtle()
    score_writer.hideturtle()
    score_writer.penup()
    score_writer.goto(100, 200)


    i = 0

    states_guessed = []

    while i < 50:
        score_writer.clear()
        score_writer.write(f'{i}/50', False, font=(FONT, FONT_SIZE, 'normal'))
        guess = screen.textinput(title=f'{i}/50 States Correct', prompt='Guess a State name? ').title()

        if guess == 'Exit':
            break

        if data['state'].str.contains(guess).any():

            if guess not in states_guessed:
                state_row = data[data.state == guess]
                states_guessed.append(guess)

                # x_cor = int(state_row.x)
                # y_cor = int(state_row.y)
                writer.goto(int(state_row.x), int(state_row.y))
                writer.write(guess)
                i += 1

    states_to_learn = {
        'State' : [],
        'x' : [],
        'y' : []
    }
    # states to learn
    states = data['state'].to_list()
    print(states)
    for row in states:
        if row not in states_guessed:
            state_row = data[data.state == row]
            states_to_learn['State'].append(row)
            states_to_learn['x'].append(int(state_row.x))
            states_to_learn['y'].append(int(state_row.y))

    df = pandas.DataFrame(states_to_learn)


    df.to_csv('./USStatesGame/states_to_learn.csv')

    screen.exitonclick()