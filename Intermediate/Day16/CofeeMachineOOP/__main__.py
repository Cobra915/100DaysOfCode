if __name__ == '__main__':
    from menu import Menu, MenuItem
    from coffee_maker import CoffeeMaker
    from money_machine import MoneyMachine
    import time
    import os

    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker()
    menu = Menu()


    machine_on = True
    valid_selections = menu.get_items().split('/')
    valid_selections.append('report')
    valid_selections.append('off')
    while '' in valid_selections:
        valid_selections.remove('')
    print(valid_selections)
    while machine_on == True:
        selection = input(f'What would you like? {menu.get_items()}: ')
        while selection not in valid_selections:
            selection = input(f'Please enter a valid selection. What would you like? ({menu.get_items()}): ')
        if selection == 'off':
            print('Powering off...')
            machine_on = False
        elif selection.lower() == 'report':
            coffee_maker.report()
            money_machine.report()
            time.sleep(2)
        else:
            drink = menu.find_drink(selection)
            if coffee_maker.is_resource_sufficient(drink):
                print(f'That will be ${drink.price}')
                if money_machine.make_payment(drink.price):
                    print('Dispensing beverage...')
                    time.sleep(2)
                    coffee_maker.make_coffee(drink)
        time.sleep(3)
        os.system('cls')