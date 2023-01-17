
from menu import MENU
import time


def run_report(inventory : dict):
    ''' Returns a report of the inventory'''
    print(
        '''
        Water: {Water} mL
        Milk: {Milk} mL
        Coffee: {Coffee} g
        Money: ${Money}
        '''.format(**inventory))
    pass

# espresso/latte/cappuccino

def make_coffee(selection : str, inventory : dict):
    price = MENU[selection]['cost']
    if inv_check(selection, inventory) == True:
        payment = proc_payment(price)
        if payment != 0:
            inventory['Money'] += payment
        else:
            return inventory
        inventory = produce_coffee(selection, inventory)
    else:
        print(f'Not enough resources to produce {selection}')
        time.sleep(3)
    
    return inventory

def proc_payment(price):
    print(f'Price: ${price}')
    denominations = {
        'quarters' : 0.25, 
        'dimes' : 0.10, 
        'nickles' : 0.05, 
        'pennies' : 0.01,
    }
    payment = 0
    for denomination in denominations:
        amount = int(input(f'How many {denomination}?: '))
        payment += amount*denominations[denomination]

    if payment >= price:
        change = round(payment - price, 2)
        payment = payment - change
        print('Processing...')
        time.sleep(1)
        print(f'Thank you! Dispensing your ${change} in change.')
    elif payment < price:
        print('Sorry, that\'s not enough money. Money refunded.')
        time.sleep(3)
        payment = 0
    return payment

def inv_check(selection, inventory):
    for ingredient in MENU[selection]['ingredients']:
        if MENU[selection]['ingredients'][ingredient] > inventory[ingredient]:
            return False
    return True

def produce_coffee(selection, inventory):
    for ingredient in MENU[selection]['ingredients']:
        inventory[ingredient] = inventory[ingredient] - MENU[selection]['ingredients'][ingredient]
    print('Dispensing beverage...')
    time.sleep(5)
    print(f'Your {selection} is ready! Please enjoy!')
    time.sleep(3)
    return inventory
        