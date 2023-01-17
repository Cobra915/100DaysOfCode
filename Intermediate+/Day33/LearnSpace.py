# APIs
MY_LOCATION = (39.695933, -104.988594)
MY_GEN_LOC_UPPER = (math.ceil(MY_LOCATION[0]), math.ceil(MY_LOCATION[1]))
MY_GEN_LOC_LOWER = (math.floor(MY_LOCATION[0]), math.floor(MY_LOCATION[1]))
MY_EMAIL = 'cobra.915.infosystems'
PASSWORD = 'fuxknzackneyrpfp'

import urllib3
import json
import math
import smtplib
from datetime import datetime  

def send_email(iss_position, date_time):
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL, 
            to_addrs=MY_EMAIL, 
            msg=f'Subject: The ISS is overhead! \n\n At {date_time}, the ISS was at {iss_position} which is within your geographical location. It should be visible in the sky.'
            )

def get_postion():
    http = urllib3.PoolManager()
    req = http.request('GET',"http://api.open-notify.org/iss-now.json")
    print(req.status)
    response = req.data
    return response

def process_response(response):

    string = response.decode('utf8')

    data = json.loads(string)

    timestamp = data['timestamp']
    iss_position = (float(data['iss_position']['latitude']), float(data['iss_position']['longitude']))
    round

    return iss_position, timestamp


if __name__ == '__main__':

    response = get_postion()

    iss_position, timestamp = process_response(response)

    date_time = datetime.fromtimestamp(timestamp)

    if MY_GEN_LOC_LOWER < iss_position < MY_GEN_LOC_UPPER:
        send_email(iss_position, date_time)