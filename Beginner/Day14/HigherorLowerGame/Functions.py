import random
from data import data
from ascii_art import vs
import time

def pick_first_contenders():
    contenders_used = []
    current_contender, next_contender = random.sample(data, 2)
    contenders_used.append(current_contender['name']) 
    contenders_used.append(next_contender['name'])
    return current_contender, next_contender, contenders_used

def pick_next_contender(contenders_used):
    next_contender = random.choice(data)
    # while next_contender['name'] in contenders_used:
    #     pick_next_contender(contenders_used)
    # contenders_used.append(next_contender['name'])
    return next_contender, contenders_used

def Compare_Contenders(current_contender, next_contender, score_count):
    print('Contender A: {name}, {description}, from {country}.'.format(**current_contender))
    print(vs)
    print('Contender B: {name}, {description}, from {country}.\n'.format(**next_contender))

    # Prints for debugging
    # print(current_contender['follower_count'])
    # print(next_contender['follower_count'])

    if current_contender['follower_count'] > next_contender['follower_count']:
        answer = 'A'
        winner = current_contender
    else: 
        answer = 'B'
        winner = next_contender

    guess = input('Who has more followers? Type \'A\' or \'B\': ')
    while guess.upper() != 'A' and guess.upper() != 'B':
        guess = input('Please enter a valid guess. Who has more followers? Type \'A\' or \'B\': ')

    if guess.upper() == answer:
        #win condition
        outcome = 'win'
        score_count += 1
        print(f'You\'re right! Current score: {score_count}\n')
        time.sleep(2)
    else:
        #lose condition
        outcome = 'loss'
        print(f'Sorry, that\'s wrong. Final score: {score_count}\n')
        print('{name} has {follower_count}'.format(**current_contender))
        print('{name} has {follower_count}'.format(**next_contender))
        time.sleep(2)
    return outcome, score_count, winner

