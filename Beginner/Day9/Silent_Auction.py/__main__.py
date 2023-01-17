if __name__ == "__main__":    
    import os
    import ascii_art
    import time

    print(ascii_art.logo)
    print('Welcome to the silent auction simulator!')

    nobody_else = False
    bid_dict = {}

    while not nobody_else:
        name = input('What is your name? ')
        bid = int(input('What is your bid? $'))

        bid_dict[name] = bid

        query = input('Is there anyone else? ')

        if query.upper() == 'NO':
            nobody_else = True

        os.system('cls')

    #highest_bid = 0
    #for bidder in bid_dict:
    #    bid_amount = bid_dict[bidder]
    #    if bid_amount > highest_bid:
    #        highest_bid = bid_amount

    winner = max(bid_dict, key=bid_dict.get)

    time.sleep(3)

    print(f'The highest bid was {winner} at ${bid_dict[winner]}!\n')