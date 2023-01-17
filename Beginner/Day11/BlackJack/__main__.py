if __name__ == "__main__":
    
    import os
    import Functions
    import ascii_art
    import time

    # the deck has an unlimited size. Meaning we're going to draw with replacement
    # There are no jokers, obvi
    # Jack, King, Queen all count as 10
    # The Ace can count as 11 or 1, depending on your holding
    # If a dealer hand values to be less than 17, they must draw again

    def GameHandler():
        print(ascii_art.logo)
        print('Welcome to my BlackJack simulator')

        i = 0
        player_hand = []
        dealer_hand = []

        while i < 2:
            player_hand = Functions.draw_card(player_hand)
            dealer_hand = Functions.draw_card(dealer_hand)
            i += 1

        loop = False

        while not loop:
            player_score = Functions.calculate_score(player_hand)
            dealer_score = Functions.calculate_score(dealer_hand)        
            Functions.display_score(player_hand, dealer_hand)

            if Functions.check(player_score, dealer_score) == True:
                loop = True
            else:
                query = input('What would you like to do? \'Hit\' or \'Stay\': ').title()
                if query == 'Hit':
                    player_hand = Functions.draw_card(player_hand)
                elif query == 'Stay':
                    loop = True
                    

        while dealer_score != 0 and dealer_score < 17:
                dealer_hand = Functions.draw_card(dealer_hand)
                dealer_score = Functions.calculate_score(dealer_hand)

        time.sleep(1)

        print(f"   Your final hand: {player_hand}, final score: {player_score}")
        print(f"   Computer's final hand: {dealer_hand}, final score: {dealer_score}")
        Functions.score(player_score, dealer_score)


    GameHandler()

    while input('Would you like to play again? ') == 'y':
        os.system('cls')
        GameHandler()

