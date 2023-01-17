import time
import selectchoice
import ascii_art
import process

def Round_Handler():

    choices = selectchoice.define_choices()

    plyrchoice = input('\nPlease make your selection ("Rock," "Paper" or "Scissors") ')
    print(f'\nYou chose {str.title(plyrchoice)}')
    plyrchoice_rep = ascii_art.represent_choice(plyrchoice.upper())
    print(plyrchoice_rep)


    time.sleep(2)

    oppchoice = selectchoice.opponent_selection(choices)
    print(f'Your opponent chose {oppchoice}')
    oppchoice_rep = ascii_art.represent_choice(oppchoice.upper())
    print(oppchoice_rep)

    time.sleep(2)

    outcome = process.evaluate_outcome(plyrchoice, oppchoice)

    time.sleep(2)

    return outcome