cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10 , 10]

import random

def draw_card(hand):
        hand.append(cards[random.randint(0, len(cards)-1)])
        if hand[-1] == 11 and sum(hand) > 21:
            hand[-1] = 1
    
        return hand

def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    return sum(hand)

    
def score(player_score, dealer_score):
    if player_score > 21:
        print('You bust!')
    elif dealer_score > 21:
        print('Dealer bust! You win!')
    elif player_score == 0:
        print('You win with a blackjack!')
    elif dealer_score == 0:
        print('Dealer wins with a blackjack, you lose')
    elif player_score <= 21 and dealer_score <= 21:
        if player_score > dealer_score:
            print('You win!')
        elif player_score == dealer_score:
            print('It\'s a draw')
        else:
            print('You lose')
    return True

def check(player_score, dealer_score):
    if player_score > 21 or player_score == 0 or dealer_score == 0:
        return True
    return False

def display_score(player_hand, dealer_hand):
    print(f'    Player hand: {player_hand} totalling {sum(player_hand)}')
    print(f'    Dealer first card: {dealer_hand[0]}')