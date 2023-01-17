   
def evaluate_outcome(plyrchoice, oppchoice):

    outcome_map = {
        'ROCKROCK' : 'draw',
        'ROCKPAPER' : 'lose',
        'ROCKSCISSORS' : 'win',
        'PAPERROCK' : 'win',
        'PAPERPAPER' : 'draw',
        'PAPERSCISSORS' : 'lose',
        'SCISSORSROCK' : 'lose',
        'SCISSORSPAPER' : 'win',
        'SCISSORSSCISSORS' : 'draw'
    }

    exchange = plyrchoice.upper() + oppchoice.upper()

    outcome = outcome_map[exchange]

    if exchange == 'ROCKPAPER' or exchange == 'PAPERROCK':
        print(f'Paper wraps Rock, you {outcome} this round.')
    elif exchange == 'ROCKSCISSORS' or exchange == 'SCISSORSROCK':
        print(f'Rock crushes Scissors, you {outcome} this round.')
    elif exchange == 'PAPERSCISSORS' or exchange == 'SCISSORSPAPER':
        print(f'Scissors cuts Paper, you {outcome} this round.')
    elif outcome == 'draw':
        print(f'{str.title(plyrchoice)} vs {oppchoice}, it\'s a draw.')

    return outcome