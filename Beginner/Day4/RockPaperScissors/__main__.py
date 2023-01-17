if __name__ == "__main__":

    import time
    import RoundHandler
    import ascii_art
    import os
    
    print('Welcome to the Rock, Paper, Scissors simulator!')

    time.sleep(2)

    round_select = int(input("How many wins would you like to play to? 3, 5 or 7? "))
    plyrscore = 0
    oppscore = 0
    round = 1
    while True:
        os.system('cls')
        time.sleep(2)

        print(f"\nRound {round}, first to {round_select} points wins!")
        print(f"the score is {plyrscore} - {oppscore}")

        time.sleep(2)

        outcome = RoundHandler.Round_Handler()

        if outcome == 'win':
            plyrscore += 1
        elif outcome == 'lose':
            oppscore += 1

        if plyrscore == round_select:
            print(f'After {round} rounds, you win the game! The final score was {plyrscore} - {oppscore}')
            ascii_art.win()
            time.sleep(2)
            print('Thanks for playing!')
            break
        elif oppscore == round_select:
            print(f'After {round} rounds, you\'ve lost :( The final score was {plyrscore} - {oppscore}')
            ascii_art.loss()
            time.sleep(2)
            print('Thanks for playing!')

            break
        round += 1