import random
import os
import time
import ascii_art

def generate_random_word(word_length):
    with open("words_alpha.txt") as f:
        word_list = f.read().splitlines()

    def generate():
        i = random.randint(0, len(word_list)-1)
        prompt = word_list[i]
        return prompt

    prompt = generate()

    while len(prompt) != word_length:
        prompt = generate()

    return prompt

def generate_puzzle_string(puzzle_word):
    puzzle_string_list = []
    for letter in range(len(puzzle_word)):
        puzzle_string_list.append('_')
    return puzzle_string_list

def update_puzzle_string(puzzle_word, guess, puzzle_string, win_count):
    for i in range(len(puzzle_word)):
        if guess == puzzle_word[i]:
            puzzle_string[i] = guess
            win_count += 1
    return puzzle_string, win_count


def print_display(loss_count, guesses, list):
    os.system('cls')
    print('==============================\n')
    print(' '.join(list))
    ascii_art.print_ascii_art(loss_count)

    print(f'Your guesses: {guesses}')
    print('==============================')

def end_print_display(loss_count, guesses, string):
    os.system('cls')
    print('==============================\n')
    print(' ' + ' '.join([*string]))
    ascii_art.print_ascii_art(loss_count)
    print(f'Your guesses: {guesses}')
    print('==============================')

def RoundHandler(puzzle_word, puzzle_string, win_count, loss_count, guesses):
    
    print_display(loss_count, guesses, puzzle_string)
    
    guess = input('Please guess a letter: ').lower()
    if guess in guesses:
        print(f'\nYou\'ve already guessed {guess}!')
        time.sleep(2)
        return win_count, loss_count, puzzle_string, guesses

    guesses.append(guess)

    if guess in puzzle_word:
        print(f'\nYou guessed {guess}, that\'s in the word!')
        time.sleep(2)
        puzzle_string, win_count = update_puzzle_string(puzzle_word, guess, puzzle_string, win_count)

    else:
        print(f'\nYou guessed {guess}, that\'s NOT in the word!')
        time.sleep(2)
        loss_count += 1

    return win_count, loss_count, puzzle_string, guesses

def end_check(win_count, loss_count, puzzle_word):
    if win_count == len(puzzle_word) or loss_count == 6:
        return True

