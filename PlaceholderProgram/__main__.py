# APIs
import urllib3
import json
import smtplib

MY_EMAIL = 'cobra.915.infosystems'
PASSWORD = 'REPLACE WITH ENV VARIABLE' 

parameters = {
    'placeholder1' : 'text',
    'placeholder2' : 'text'
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

def get_request_1():
    http = urllib3.PoolManager()
    req = http.request('GET',"http://api.open-notify.org/iss-now.json")
    print(f'ISS Position API request status: {req.status}')
    response = req.data

    return response

def get_request_2():
    http = urllib3.PoolManager()
    req = http.request('GET',"https://api.sunrise-sunset.org/json", fields=parameters)
    print(f'Sunrise/Sunset API request status: {req.status}')
    response = req.data
    string = response.decode('utf8')
    data = json.loads(string)
    return

def process_response(response):

    string = response.decode('utf8')

    data = json.loads(string)




if __name__ == '__main__':
    pass
