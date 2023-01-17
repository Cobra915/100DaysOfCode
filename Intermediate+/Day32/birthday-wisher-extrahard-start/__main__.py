import pandas
import smtplib
import random
import datetime as dt
import os

MY_EMAIL = os.environ['INFO_SYS_EMAIL_USER']
PASSWORD = os.environ['INFO_SYS_EMAIL_PW']

def parse_input():
    data = pandas.read_csv('./birthday-wisher-extrahard-start/birthdays.csv')
    data_dict = data.to_dict(orient='records')

    return data_dict

def send_email(txt, address):
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=address, 
            msg=f'Subject: Happy Birthday! \n\n {txt}'
            )

def form_age_str(age):
    if str(age)[-1] == '1':
        age_str = str(age) + 'st'
    elif str(age)[-1] == '2':
        age_str = str(age) + 'nd'
    elif str(age)[-1] == '3':
        age_str = str(age) + 'rd'
    else:
        age_str = str(age) + 'th'
    return age_str

def modify_message(name, age_str):
    path = f'./birthday-wisher-extrahard-start/letter_templates/letter_{random.randint(1,3)}.txt'
    with open(path) as fin:
        txt = fin.read()
    new_txt = txt.replace('[NAME]', name)
    new_txt = new_txt.replace('[AGE]', age_str)
    return new_txt

if __name__ == '__main__':

    today = dt.datetime.today()
    comparator = (today.month, today.day)
    data = parse_input()

    for row in data:

        date_of_birth = dt.datetime(year=row['year'],month=row['month'],day=row['day'])
        dob_tuple = (row['month'], row['day'])
        if comparator == dob_tuple:
            name = row['name']
            email = row['email']
            age = int(today.year) - int(row['year'])
            age_str = form_age_str(age)
            txt = modify_message(name, age_str)

            send_email(txt, email)
            # ouput
            print(f'Today is {name}\'s {age_str} birthday. Sending birthday email to {email}')
