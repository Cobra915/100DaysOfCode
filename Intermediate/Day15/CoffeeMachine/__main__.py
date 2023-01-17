if __name__ == '__main__':
    '''
    1. Prompt user by asking "What would you like? (espresso/latte/cappuccino): "
    2. Turn off the coffee machine by entering 'off' to the prompt - so while input != 'off'
    3. Print report - return supply values and money
    4. Check resources sufficient?
    5. Process coins - request input of coins to equal total cost of coffee requested
    6. Check transaction successful
    7. Make coffee
    8. Primary while loop
    9. Cleanup and add timers
    '''

    import Functions
    import time
    import os

    inventory = {
        'Water' : 300,
        'Milk' : 200,
        'Coffee' : 100,
        'Money' : 0,
    }

    machine_on = True
    valid_selections = ['espresso', 'latte', 'cappuccino', 'report', 'off']
    while machine_on == True:
        selection = input('What would you like? (espresso/latte/cappuccino): ')
        while selection not in valid_selections:
            selection = input('Please enter a valid selection. What would you like? (espresso/latte/cappuccino): ')
        if selection == 'off':
            print('Powering off...')
            machine_on = False
            time.sleep(2)
        elif selection.lower() == 'report':
            Functions.run_report(inventory)
            time.sleep(6)
        else:
            inventory = Functions.make_coffee(selection, inventory)
        os.system('cls')
        


