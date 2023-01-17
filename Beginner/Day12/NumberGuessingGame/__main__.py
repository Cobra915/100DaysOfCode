if __name__ == '__main__':

    import os
    import Functions

    Functions.NumberGuesser()

    while input('Would you like to play again? \'Y/N\'') == 'Y':
        os.system('cls')
        Functions.NumberGuesser()