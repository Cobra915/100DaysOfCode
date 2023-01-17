# APIs
import urllib3
import json
import smtplib
from pprint import pprint
from twilio.rest import Client
import os

MY_LOCATION = (39.695933, -104.988594)
MY_LAT = MY_LOCATION[0]
MY_LON = MY_LOCATION[1]
URI = 'https://api.openweathermap.org/data/2.5/onecall'

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
api_key = os.environ['OWM_API_KEY']

parameters = {
    'lat' : MY_LAT,
    'lon' : MY_LON,
    'exclude' : 'current,daily,minutely',
    'appid' : api_key
}

def get_request_2():
    http = urllib3.PoolManager()
    req = http.request('GET',URI, fields=parameters)
    print(f'OpenWeatherMap API call status: {req.status}')
    response = req.data
    return response

def process_response(response):

    string = response.decode('utf8')

    data = json.loads(string)
    return data

def process_data(data):
    weather_slice = data['hourly'][:12]
    conditions = [hour['weather'][0]['id'] for hour in weather_slice]
    print = conditions
    for condition in conditions:
        if 600 <= condition <= 622:
            message_text = f'It is going to rain today starting in {conditions.index(condition)} hours. Bring an umbrella!'
            send_text(message_text)
            break

def send_text(message_text):
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=message_text,
            from_='+12538679308',
            to='+13144401242'
    )

    print(message.status)


if __name__ == '__main__':
    response = get_request_2()
    data = process_response(response)
    process_data(data)
