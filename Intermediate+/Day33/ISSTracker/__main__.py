# APIs
import urllib3
import json
import smtplib
from datetime import datetime
import os

MY_LOCATION = (39.695933, -104.988594)
MY_LAT = MY_LOCATION[0]
MY_LNG = MY_LOCATION[1]
MY_EMAIL = os.environ['INFO_SYS_EMAIL_USER']
PASSWORD = os.environ['INFO_SYS_EMAIL_PW']

parameters = {
    'lat' : MY_LAT,
    'lng' : MY_LNG,
    'formatted' : 0
}

def send_email(iss_position, iss_time):
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs='crbradshaw93@gmail.com', 
            msg=f'Subject: The ISS is overhead! \n\nAt {iss_time}, the ISS was at {iss_position} which is within your geographical location. It should be visible in the  night sky.'
            )

def get_postion():
    http = urllib3.PoolManager()
    req = http.request('GET',"http://api.open-notify.org/iss-now.json")
    print(f'ISS Position API request status: {req.status}')
    response = req.data

    return response

def get_sunrise_sunset():
    http = urllib3.PoolManager()
    req = http.request('GET',"https://api.sunrise-sunset.org/json", fields=parameters)
    print(f'Sunrise/Sunset API request status: {req.status}')
    response = req.data
    string = response.decode('utf8')
    data = json.loads(string)

    sunrise_form = data['results']['sunrise']
    sunrise_hour = int(sunrise_form.split('T')[1].split(':')[0])

    sunset_form = data['results']['sunset']
    sunset_hour = int(sunset_form.split('T')[1].split(':')[0])

    return sunrise_hour, sunset_hour

def process_response(response):

    string = response.decode('utf8')

    data = json.loads(string)

    timestamp = data['timestamp']
    iss_position = (float(data['iss_position']['latitude']), float(data['iss_position']['longitude']))
    date_time = datetime.fromtimestamp(timestamp)
    date_time_str = str(date_time)
    iss_time = date_time_str.split(' ')[1]
    iss_lat = iss_position[0]
    iss_lng = iss_position[1]

    return iss_position, iss_time, iss_lat, iss_lng

def is_night(sunset_hour, sunrise_hour):
    time_now = datetime.now()
    time_hour = time_now.hour
    if sunset_hour <= time_hour or time_now <= sunrise_hour:
        return True

def iss_in_pos(iss_lat, iss_lng):
    if MY_LAT-5 <= iss_lat <= MY_LAT+5 and MY_LNG-5 <= iss_lng <= MY_LNG+5:
        return True

if __name__ == '__main__':
    while True:
        response = get_postion()

        iss_position, iss_time, iss_lat, iss_lng = process_response(response)

        sunrise_hour, sunset_hour = get_sunrise_sunset()

        if iss_in_pos(iss_lat, iss_lng) and is_night(sunset_hour, sunrise_hour):
                send_email(iss_position, iss_time)