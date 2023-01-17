import os
import time

def add(n1, n2):
        return n1 + n2
 
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculate(n1 ,n2, operator):
    operator_dict = {
        '+' : add(n1, n2),
        '-' : subtract(n1, n2),
        '*' : multiply(n1, n2),
        '/' : divide(n1, n2),
    }
    return operator_dict[operator]

#def Calculator():
#    n1 = float(input('What\'s the first number?: '))
#    end = False
#    while not end:
#        operator = input('\n+\n-\n*\n/\nPick an operation: ')
#        n2 = float(input('What\'s the next number?: '))
#        output = calculate(n1, n2, operator)
#        print(f'{n1} {operator} {n2} = {output}')
#        proceed = input(f'Type \'y\' to continue caluclating with {output}, type \'n\' to start a new calculation or type \'esc\' to quit: ')
#        proc_end = False
#        while not proc_end:
#            if proceed == 'y':
#                n1 = output
#                proc_end = True
#            elif proceed == 'n':
#                return False
#            elif proceed == 'esc':
#                return True
#            else:
#                proceed = input(f'Please enter a valid input: \'y\' to continue caluclating with {output}, \'n\' to start a new calculation or \'esc\' to quit: ')
#                proc_end = False
#            os.system('cls')

def Calculator():
    n1 = float(input('What\'s the first number?: '))
    end = False
    while not end:
        operator = input('\n+\n-\n*\n/\nPick an operation: ')
        n2 = float(input('What\'s the next number?: '))
        output = calculate(n1, n2, operator)
        print(f'{n1} {operator} {n2} = {output}')
        proceed = input(f'Type \'y\' to continue caluclating with {output}, type \'n\' to start a new calculation or type \'esc\' to quit: ')
        proc_end = False
        while not proc_end:
            if proceed == 'y':
                n1 = output
                proc_end = True
            elif proceed == 'n':
                proc_end = True
                end = True
                Calculator()
            elif proceed == 'esc':
                proc_end = True
                end = True
                print('Exiting...')
                time.sleep(2)
                #quit()
            else:
                proceed = input(f'Please enter a valid input: \'y\' to continue caluclating with {output}, \'n\' to start a new calculation or \'esc\' to quit: ')
                proc_end = False
            os.system('cls')