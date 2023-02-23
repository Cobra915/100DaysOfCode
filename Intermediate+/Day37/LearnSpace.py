import urllib3
import logging
import json
import os

# Habit Tracking Project: API Post Requests & Headers

# HTTP Requests

# - GET
# - POST - We gitve the API a piece of data, we're not concerned with teh outcome, other than knowing it was successful
# - PUT - PUT is where you update a piece of data in an external system
# - DELETE - Delete a piece of data from an external system
METHOD = ''
log_path = os.getcwd() + "\debug.log"

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

# Define functions
def stock_get_request(method, ENDPOINT, parameters):
    http = urllib3.PoolManager()
    req = http.request(METHOD, ENDPOINT, fields=parameters)
    logging.info(f'Stocks API call returned with status: {req.status}')
    response = req.data
    string = response.decode('utf8')

    data = json.loads(string)
    return data

cwd = os.getcwd()
log_path = cwd + "\debug.log"
logging.info(f"Testing logging by using an os func to get current working dir and appending debug.log to it so I don't have to reconfigure the file path every time, leaving us with {log_path}")
print("Current working directory: {0}".format(log_path))

