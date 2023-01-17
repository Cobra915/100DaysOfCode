import random

def define_choices():
    choices = ['Rock', 'Paper', 'Scissors']
    return choices

def opponent_selection(choices):
    choice = choices[random.randint(0,len(choices)-1)]
    return choice

    
