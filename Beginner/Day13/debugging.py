############DEBUGGING#####################

# Describe Problem - This one won't run on iteration 20, 
# def my_function():
#   #for i in range(1, 20):
#   for i in range(1, 21):
    # if i == 20:
    #   print("You got it")
# my_function()

# # Reproduce the Bug -- This had the the randint ranges wrong, it would have taken the list index out of range on six and since it started at 1, the first item would never be selected.
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# # dice_num = randint(1, 6)
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# # Play Computer -- one of the below needs a >=/<= on the 1994 component. If year is 1994, you'll have a conflict.
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# #elif year > 1994:
# elif year >= 1994:
#   print("You are a Gen Z.")

# # Fix the Errors -- indent issue on the print line under the if. Input was not being converted to int type. The print line was not a formatted string, also 18 is not driving age in the US, it's 16
# age = int(input("How old are you?"))
# #if age > 18:
# #print("You can drive at age {age}.")
# if age >= 16:
#     print(f"You can drive at age {age}.")

# #Print is Your Friend -- there's a conditional comparator on the word_per_page line. You also don't need to define the varibles beforehand because they're defined by inputs, it's redundant.
# # pages = 0
# # word_per_page = 0
# pages = int(input("Number of pages: "))
# # word_per_page == int(input("Number of words per page: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger -- indentation issue, the append was not under the for loop so it wasn't being comnpleted until the last iteration.
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   # b_list.append(new_item)
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])