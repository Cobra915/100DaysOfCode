import random
import string

def generate_letters(letter_length, pw):
    letter_choices = string.ascii_letters
    for letter in range(letter_length):
        letter = random.choice(letter_choices)
        pw.append(letter)
    return pw

def generate_symbols(symbol_length, pw):
    symbol_choices = string.punctuation
    for symbol in range(symbol_length):
        pw.insert(random.randint(0, len(pw)), random.choice(symbol_choices))
    return pw

def generate_numbers(number_length, pw):
    number_choices = string.digits
    for number in range(number_length):
        pw.insert(random.randint(0, len(pw)), random.choice(number_choices))
    return pw
    

