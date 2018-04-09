#import requests

def get_stock_price(symbol):
    url = f'https://api.iextrading.com/1.0/stock/{symbol}/batch?types=quote'
    r = requests.get(url)
    json_response = r.json()
    return json_response['quote']['latestPrice']

def get_crypto_price(symbol):
    url = f'https://min-api.cryptocompare.com/data/price?fsym={symbol}&tsyms=USD'
    r = requests.get(url)
    json_response = r.json()
    return json_response['USD']
