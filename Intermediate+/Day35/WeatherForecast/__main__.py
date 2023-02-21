import urllib3
import json
from twilio.rest import Client
import logging
import logging.handlers
import boto3

'''
TODO
- Improve logging
- Improve message text output
'''

# Setting up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("./WeatherForecast/debug.log"),
        # logging.StreamHandler()
    ]
)
# End logging setup

# Define variable and constants
MY_LOCATION = (39.695933, -104.988594)
MY_LAT = MY_LOCATION[0]
MY_LON = MY_LOCATION[1]
URI = 'https://api.openweathermap.org/data/2.5/onecall'

ssm = boto3.client('ssm')

account_sid = ssm.get_parameter(Name='/Python/TWILIO_ACCOUNT_SID', WithDecryption=True)['Parameter']['Value']
auth_token = ssm.get_parameter(Name='/Python/TWILIO_AUTH_TOKEN', WithDecryption=True)['Parameter']['Value']
api_key = ssm.get_parameter(Name='/Python/OWM_API_KEY', WithDecryption=True)['Parameter']['Value']

parameters = {
    'lat' : MY_LAT,
    'lon' : MY_LON,
    'exclude' : 'current,daily,minutely',
    'appid' : api_key
}
# End variables and constants

# Define functions
def get_request_2():
    http = urllib3.PoolManager()
    req = http.request('GET',URI, fields=parameters)
    logging.info(f'OpenWeatherMap API call status: {req.status}')
    response = req.data
    return response

def process_response(response):

    string = response.decode('utf8')

    data = json.loads(string)

    return data

def process_data(data):
    weather_slice = data['hourly'][:12]
    conditions = [hour['weather'][0]['id'] for hour in weather_slice]
    conditions_print = [hour['weather'][0]['description'] for hour in weather_slice]
    logging.info(f'conditions: {conditions_print}')
    i=0
    for condition in conditions:
        if 600 <= condition <= 622:
            message_text = f'It is going to snow today starting in {conditions.index(condition)} hours. Stay warm!'
            logging.info(f'Snow in hour {i} with id: {condition} - {conditions_print[i]}, calling send_text()')
            send_text(message_text)
            break
        else:
            logging.info(f'Snow not in hour: {i} with id: {condition} - {conditions_print[i]} continuing')
        i+=1

def send_text(message_text):
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=message_text,
            from_='+12538679308',
            to='+13144401242'
    )

    logging.info(f'twilio client call succeeded with message: {message.status}')
# End functions

# Implementation
if __name__ == '__main__':
    response = get_request_2()
    data = process_response(response)
    process_data(data)