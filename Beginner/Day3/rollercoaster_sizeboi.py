import string

print("Welcome to he rollercoaster!")
height = int(input("Wait, how tall are you? (in cm) "))
bill = 0

if height >= 120:
    age = int(input("Okay sick, wait how old are you? "))
    if age >= 18:
        bill += 12
        print("That'll be $12, you weirdo. You know this rollercoaster is for kids, right?")
    elif age < 12:
        bill += 5
        print("That'll be $5, twerp")
    elif age >= 45 and age <= 55: 
        print("awww, what's wrong? Sad about being old? It's okay big-baby here's a free ride on us")
    else:
        bill += 7
        print("That'll be $7, you dumb teen Go make a tiktok in public while everyone watches you, wishing murder was legal.")
    
    Photos = input("I would like to take photos of you, do you consent? Y or N. ")
    if Photos == "Y":
        bill += 3
        print("Oh yes, I can't wait to look at photos of you later.")
    else: 
        print("Damn, *whispers under breath* I'll get pictures of you somehow")

    print(f'your final bill is ${bill}')
    print("Here's your ticket. Have fun standing in that line, nerd!")


else: 
    print("You little IDIOT, why are you so small? Sorry, SHRIMP, you gotta come back when you've grown taller. Go cry to your mom like a little whiney baby!")