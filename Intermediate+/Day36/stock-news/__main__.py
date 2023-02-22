import urllib3
import json
from twilio.rest import Client
import logging
import logging.handlers
import os
from pprint import pprint

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
av_api_key = os.environ['AV_API_KEY']
nao_api_key = os.environ['NAO_API_KEY']


stock_parameters = {
    'function' : 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol' : STOCK_NAME,
    'apikey' : av_api_key,
    'datatype' : 'json'
}

news_parameters = {
    'qInTitle' : COMPANY_NAME,
    'apiKey' : nao_api_key,
}

# Setting up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("./stock-news/debug.log"),
        # logging.StreamHandler()
    ]
)
# End logging setup

# Define functions
def stock_get_request(ENDPOINT, parameters):
    http = urllib3.PoolManager()
    req = http.request('GET',ENDPOINT, fields=parameters)
    logging.info(f'Stocks API call returned with status: {req.status}')
    response = req.data
    string = response.decode('utf8')

    data = json.loads(string)
    return data

def news_get_request(ENDPOINT, parameters):
    http = urllib3.PoolManager()
    req = http.request('GET',ENDPOINT, fields=parameters)
    logging.info(f'News API call returned with status: {req.status}')
    response = req.data
    string = response.decode('utf8')
    data = json.loads(string)
    focus_data = data['articles']
    return focus_data

def process_stock(data):
    daily_data = data['Time Series (Daily)']

    focus = [value for (key,value) in daily_data.items()]

    yesterday_close = float(focus[0]['4. close'])
    ereyesterday_close = float(focus[1]['4. close'])

    diff = yesterday_close - ereyesterday_close
    percentage_diff = round((abs(diff)/ereyesterday_close)*100, 2)

    if diff > 0:
        symbol = '🔺'
    else:
        symbol = '🔻'

    rep_string = symbol + str(percentage_diff) + '%'

    logging.info(f'The net change in price is {diff} which is a {percentage_diff} percent change')

    return rep_string, percentage_diff

def send_text(message_text):
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=message_text,
            from_='+12538679308',
            to='+13144401242'
    )

    logging.info(f'twilio client call succeeded with message: {message.status}')


if __name__ == '__main__':
    data = stock_get_request(STOCK_ENDPOINT, stock_parameters)
    rep_string, percentage_diff = process_stock(data)

    if percentage_diff > 5:
        logging.info(f'The stock price percent difference is {percentage_diff} which is greater than 5%, calling news_get_request()')
        articles = news_get_request(NEWS_ENDPOINT, news_parameters)
        article_focus = articles[:3]

        formatted_articles = [f"{STOCK_NAME}: {rep_string}\nHeadline:{article['title']}\nBrief:{article['description']}" for article in article_focus]
    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages.create(
                body=article,
                from_='+12538679308',
                to='+13144401242'
            )
        logging.info(f'twilio client call succeeded with message: {message.status}')



