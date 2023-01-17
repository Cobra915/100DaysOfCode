if __name__ == '__main__':
    import Functions
    import ascii_art
    import data
    import os
    import time

    print(ascii_art.logo)

    score_count = 0

    current_contender, next_contender, contenders_used = Functions.pick_first_contenders()
    outcome, score_count, winner = Functions.Compare_Contenders(current_contender, next_contender, score_count)
    if outcome == 'win':
            current_contender = winner
    else:
        print('Exiting...')
        time.sleep(2)
        exit()

    while len(contenders_used) < len(data.data):
        os.system('cls')
        print(ascii_art.logo)
        print(f'Current score: {score_count}\n')
        next_contender, contenders_used = Functions.pick_next_contender(contenders_used)
        while next_contender['name'] in contenders_used:
            next_contender, contenders_used = Functions.pick_next_contender(contenders_used)
        contenders_used.append(next_contender['name'])
        outcome, score_count, winner = Functions.Compare_Contenders(current_contender, next_contender, score_count)
        if outcome == 'win':
            current_contender = winner
        else: 
            break

    if score_count == 49:
        print('You\'ve correctly compared all of the contenders in our database! You win!\n')
        time.sleep(3)

    print('Exiting...')