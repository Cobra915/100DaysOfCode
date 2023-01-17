print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1 = input("You're at a cross road. Where do you want to go? Type 'left' or 'right' ")
if choice1.lower() == 'left':
    choice_left_2 = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. ')
    if choice_left_2.lower() == 'wait':
        choice_left_3 = input('You arrive at the island unharmed. There is a house with 3 doors. Onered, one yellow and one blue. Which color do you choose? ')
        if choice_left_3.lower() == 'yellow':
            print('You win!')
        elif choice_left_3.lower() == 'blue':
            print('It is a room full of girls that only want to give you blue balls. You die of blue balls, game over.')
        else:
            print('You cannot follow directions, you die of being incompetenet. Game over.')
    else:
        print('You attempt to swim across but the tides are too string, you\'re sucked out into a riptide and drown in the briney deep. Game over.')

else:
    print('You turn right down a long winding road. It leads to a forest. You pass through the brush into a peaceful forest glen. It is here that you are raped and murdered by Christmas critters. Game over.')