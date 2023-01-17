# list comprehension
numbers = [1, 2, 3]
list_1 = []
for n in numbers:
    add_1 = n + 1
    list_1.append(add_1)

list_2 = [n+1 for n in numbers]
print(list_2)

list_3 = [i*2 for i in range(1,6)]
print(list_3)

# # conditional list comprehension
# new_list = [new_item for item in list if test]
names = ['Alex', 'Beth', 'Carolina', 'Dave', 'Eleanor', 'Freddie']
list_4 = [name for name in names if len(name) < 5]
print(list_4)

list_5 = [name.upper() for name in names if len(name)>4]
print(list_5)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

result = {word:len(word) for word in sentence.split()}

print(result)

# dict comp
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict}

#### dict comp for weather
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

def f_conv(temp_c):
    temp_f = (temp_c*9/5)+32
    return temp_f

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#weather_f = {day : f_conv(weather_c[day]) for day in days}
weather_f = {day:f_conv(temp_c) for (day, temp_c) in weather_c.items()}
print(weather_f)

import pandas

student_dict = {
    'student':['Angela', 'James', 'Lily'],
    'score': [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

#You could loop through all the values in the data frame with a for loop
for (key, value) in student_data_frame.items():
    print(value)
# This isn't very useful

# Looop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row)