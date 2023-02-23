# Import Modules
import urllib3
import json
import smtplib
import os
import logging
from twilio.rest import Client
from datetime import datetime
# End Import Modules

# Define Constants / Variables
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = 'cobra915'


user_parameters = {
    'username' : 'cobra915',
    'agreeTermsOfService' : 'yes',
    'notMinor' : 'yes'
}

graph_config = {
    'id' : 'graph1',
    'name' : 'Coding Graph',
    'unit' : 'minutes',
    'type' : 'int',
    'color' : 'momiji'
}

date = datetime.today().strftime('%Y%m%d')

body = {
    'date' : date,
    'quantity' : input('Please input the number of minutes you have coded today (int): '),

}

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
pixela_api_key = os.environ['PIXELA_API_KEY']

graph_endpoint = f'{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1'


log_path = os.getcwd() + "\debug.log"
# End Define Constants / Variables

# Setting up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(log_path),
        # logging.StreamHandler()
    ]
)
# End logging setup

# Define Functions
def get_request(endpoint, parameters):
    http = urllib3.PoolManager()
    req = http.request('GET',endpoint, json=parameters)
    logging.info(f'{endpoint} API request status: {req.status}')
    response = req.data
    string = response.decode('utf8')
    data = json.loads(string)

    return data

def post_request(endpoint, body):
    encoded_body = json.dumps(body)
    http = urllib3.PoolManager()
    req = http.request('POST',endpoint, headers={'Content-Type': 'application/json', 'X-USER-TOKEN' : pixela_api_key},
                 body=encoded_body)
    logging.info(f'{endpoint} API request status: {req.status}')
    response = req.data
    string = response.decode('utf8')
    data = json.loads(string)
    return data

# End Define Functions

# Implementation
if __name__ == '__main__':
    response = post_request(graph_endpoint, graph_config)
    print(response)
