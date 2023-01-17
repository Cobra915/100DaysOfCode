import smtplib
import random
import datetime as dt
import os

MY_EMAIL = os.environ['INFO_SYS_EMAIL_USER']
PASSWORD = os.environ['INFO_SYS_EMAIL_PW']

def parse_input():
    with open(file = './MondayMotivation/quotes.txt') as fin:
        quotes = fin.readlines()
    quote = random.choice(quotes)

    with open(file = './MondayMotivation/addresses.txt') as fin:
        addresses = fin.readlines()

    return quote, addresses

def send_email(quote, address):
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=address, 
            msg=f'Subject: Monday Motivation \n\n {quote}'
            )


if __name__ == '__main__':

    now = dt.datetime.now()
    day_of_week = now.weekday()
    if day_of_week == 0:

        quote, addresses = parse_input()
        for address in addresses:
            send_email(quote, address)
