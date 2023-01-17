'''In the next lesson, I'll show you how to send email using the smtplib module and Python. If you are getting the error Connection unexpectedly closed, it might be due to a number of things. You can come back to this lesson to debug.

1. Make sure you've got the correct smtp address for your email provider:

Gmail: smtp.gmail.com

Hotmail: smtp.live.com

Outlook: outlook.office365.com

Yahoo: smtp.mail.yahoo.com

If you use another email provider, just Google for your email provider e.g. "Gmail SMTP address"



Below are steps specific to users sending email from Gmail addresses.

2. Make sure you've enabled less secure apps if you are sending from a Gmail account. (Refer to the video in the next lesson for steps).

3. Try to go through the Gmail Captcha here while logged in to the Gmail account: https://accounts.google.com/DisplayUnlockCaptcha

4. Add a port number by changing your code to this:

smtplib.SMTP("smtp.gmail.com", port=587) '''

import datetime as dt
import pandas

def parse_input():
    data = pandas.read_csv('./birthday-wisher-extrahard-start/birthdays.csv')
    data_dict = data.to_dict(orient='records')
    return data_dict

now = dt.datetime.now()
year = now.year
month = now.month
minute = now.min
day = now.day
day_of_week = now.weekday()
today = dt.datetime.today()

data = parse_input()
comparator = dt.datetime(year=today.year, month=today.month, day = today.day)
for row in data:
    print(row)
    date_of_birth = dt.datetime(year=row['year'],month=row['month'],day=row['day'])
    if date_of_birth.month == comparator.month and date_of_birth.day == comparator.day:
        age = int(comparator.year) - int(row['year'])
        print(age)
