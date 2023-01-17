#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

import time
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# with open('./MailMergeProject/Input/Names/invited_names.txt') as fin:
names = [line.rstrip() for line in open('./MailMergeProject/Input/Names/invited_names.txt')]

print(names)

for name in names:
    with open('./MailMergeProject/Input/Letters/starting_letter.txt') as fin:
        txt = fin.read()

    new_txt = txt.replace('[name]', name)
    time.sleep(2)
    print(new_txt)

    

    with open(f'./MailMergeProject/Output/ReadyToSend/letter_for_{name}.txt', mode='w') as fin:
        fin.write(new_txt)