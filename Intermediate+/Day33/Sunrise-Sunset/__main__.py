MY_LOCATION = (39.695933, -104.988594)

lat = MY_LOCATION[0]
lng = MY_LOCATION[1]

parameters = {
    'lat' : lat,
    'lng' : lng,
    'formatted' : 0
}

import urllib3
import json
from pprint import pprint

def get_sunrise_sunset():
    http = urllib3.PoolManager()
    req = http.request('GET',"https://api.sunrise-sunset.org/json", fields=parameters)
    print(req.status)
    response = req.data
    string = response.decode('utf8')
    data = json.loads(string)
    pprint(data)

    sunrise_form = data['results']['sunrise']
    sunrise_hour = sunrise_form.split('T')[1].split(':')[0]

    sunset_form = data['results']['sunset']
    sunset_hour = sunset_form.split('T')[1].split(':')[0]

    

    print(f'The sunrise will be at {sunrise_hour}')
    print(f'The sunset will be at {sunset_hour}')

    return sunrise_hour, sunset_hour

if __name__ == '__main__':
    get_sunrise_sunset()