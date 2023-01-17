import ascii_art
import random

def set_difficulty():
    '''This function will prompt the user to select a difficulty. Depending on their input, it will set and return the number of tries they're allotted for the game.'''
    difficulty = input('Choose a difficulty. Type \'easy\' or \'hard\': ')
    while difficulty != 'easy' and difficulty != 'hard':
        difficulty = input('Choose a difficulty. Type \'easy\' or \'hard\': ')

    if difficulty == 'easy':
        i = 10
    else:
        i = 5
    return i

def GameHandler(number : int, i : int):
    '''This function is the handler for the game. It will prompt the user for guesses while they still have tries and check them against the random number generated.'''
    while i != 0:
        print(f'You have {i} attempts remaining to guess the number.')
        guess = input('Make a guess: ')
        while guess.isnumeric() == False:
            guess = input('Make a valid guess: ')
        guess = int(guess)
        if guess == number:
            print(f'You got it! The answer was {number}')
            break
        GuessCheck(guess, number)
        i -= 1

    if i == 0:
        print(f'You have run out of guesses, you lose. The number was {number}')

def GuessCheck(guess : int, number : int):
    '''This function will simply check the passed in guess against the passed in number. It will give feedback on whether the guess was too high or too low.'''
    if guess > number:
        print('Too high.')
    elif guess < number:
        print('Too low.')

def NumberGuesser():
    '''This is the main game function, it will print art, set diffculty, run through the guessing loop and print the outcome.'''
    print(ascii_art.logo)
    print('Welcome to the Number Guessing Game!')

    difficulty = set_difficulty()

    number = random.randint(0,100)

    GameHandler(number, difficulty)