if __name__ == "__main__":
    
    import time
    import Functions
    import ascii_art
    import os

    print(ascii_art.logo)

    print('Welcome to my hangman game!')
    time.sleep(3)
    word_length = int(input('Before we start, how long would you like the puzzle word to be? (In letters): '))
    puzzle_word = Functions.generate_random_word(word_length)

    puzzle_string = Functions.generate_puzzle_string(puzzle_word)
    win_count = 0
    loss_count = 0
    guesses = []

    print("Thanks! Okay here we go!")

    time.sleep(2)

    while not Functions.end_check(win_count, loss_count, puzzle_word):

        win_count, loss_count, puzzle_string, guesses = Functions.RoundHandler(puzzle_word, puzzle_string, win_count, loss_count, guesses)

    if win_count == len(puzzle_word):
        Functions.end_print_display(loss_count, guesses, puzzle_word)
        print(f'The word was {puzzle_word}, congratulations, you win!')
        time.sleep(2)
        print(f'Thanks for playing!')
        time.sleep(3)
    elif loss_count == 6:
        Functions.end_print_display(loss_count, guesses, puzzle_word)
        print(f'You lose, the word was {puzzle_word}.')
        time.sleep(2)
        print(f'Thanks for playing!')
        time.sleep(3)