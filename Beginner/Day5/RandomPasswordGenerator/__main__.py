if __name__ == "__main__":

    import Functions
    import time

    pw = []
    letter_length = int(input('How many letters would you like to be in your password? '))
    symbol_length = int(input('How many symbols would you like to be in your password? '))
    number_length = int(input('How many numbers would you like to be in your password? '))
    pw_length = letter_length+symbol_length+number_length

    print(f'Your password will be {pw_length} characters long')

    time.sleep(3)

    pw = Functions.generate_letters(letter_length, pw)
    pw = Functions.generate_symbols(symbol_length, pw)
    pw = Functions.generate_numbers(number_length, pw)

    pw_final = ''.join(pw)

    print(f'Your password is: {pw_final}')