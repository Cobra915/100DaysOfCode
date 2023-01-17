# FileNotFound Exception - reading a file that doesn't exist
# with open('file.txt') as fin:
#     fin.read()

# We get:
'''
FileNotFoundError: [Errno 2] No such file or directory: 'file.txt'
'''

# KeyError Exception - indexing a dict by a nonexistant key
# a_dictionary = {'key':'value'}
# value = a_dictionary['non_existant_key']

'''
value = a_dictionary['non_existant_key']
        ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^
KeyError: 'non_existant_key'
'''

# IndexError
# fruit_list = ['Apple', 'Banana', 'Pear']
# fruit = fruit_list[3]

'''
fruit = fruit_list[3]
        ~~~~~~~~~~^^^
IndexError: list index out of range
'''

#TypeError
# text = 'abc'
# print(text + 5)

'''
print(text + 5)
      ~~~~~^~~
TypeError: can only concatenate str (not "int") to str
'''

# try: # something that might cause an exception
#     pass

# except: # do this if there was an exception
#     pass

# else: # do this is there were no exceptions
#     pass
# finally: # Do this no matter what happens
#     pass 

# let's revisit the above exceptions
# FileNotFound Exception - reading a file that doesn't exist
# try:
#     with open('file.txt') as fin:
#         fin.read()
# except:
#     print('file not found')

'''
file not found
'''

#instead of printing, we'll create the file
# try:
#     with open('file.txt') as fin:
#         fin.read()
#         a_dict = {'key':'value'}
#         print(a_dict['abc'])
# except: # you shouldn't do this, it's too braod an exception catch. it will catch all errors. 
#         #Say that file.txt exists, and gets opened, the dict with be created and indexed incorrectly. That error will be caught by the exception which will open the file or create it below. Never have a blank excepty line
#     open('file.txt', 'w')
#     fin.write('Something')

# We can fix this by writing the following:
# try:
#     fin = open('file.txt')
#     a_dict = {'key':'value'}
#     print(a_dict['key'])
# except FileNotFoundError: # Now this will be the exception action if this error occurs
#     fin = open('file.txt', 'w')
#     fin.write('Something')

# # If you want to get ahold of the error message that was thrown by py:
# except KeyError as error_message:
#     print(f'Exception caught: The key {error_message} does not exist')

# else:
#     content = fin.read()
#     print(content)

# finally:
#     if 'idk' not in content:
#         raise TypeError('I made this up')


# height = float(input('Height (in m): '))
# weight = int(input('Weight (in kg): '))

# bmi = weight / height ** 2
# print(bmi)

# if height > 3:
#     raise ValueError('no way you\'re that tall, a human height cannot be more than 3 meters')

website = 'amazon.com'
email_username = 'Cobra915'
password = 'test'

new_data = {
        website : {
            'email' : email_username, 
            'password' : password
        } 
    }

pw_dict = {}

pw_dict.append(new_data)