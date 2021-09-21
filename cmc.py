import json
import requests
import threading
import os
import dotenv
from dotenv import dotenv_values
config = dotenv_values(".env")

dotenv.load_dotenv()
API_KEY = os.environ.get('API_KEY')




url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': config.get("API_KEY")
}


def coindata(symbol):
    apiurl = 'https://pro-api.coinmarketcap.com'
    grvturl = apiurl + '/v1/cryptocurrency/quotes/latest'
    parameters = {'symbol': symbol}
    session = requests.Session()
    session.headers.update(headers)
    r = session.get(grvturl, params=parameters)
    data = r.json()['data'][symbol]
    return data

def startup():
    threading.Timer(600, startup).start()
    coindata = {
        "price": price(),
        "supply": supply(),
        "singleprice": singleprice(),
        "btcprice": btcprice(),
        "ethprice": ethprice(),
        "volume24h": volume24h(),
        "source": source()
    }
    with open("coindata.json", "w") as f:
        f.seek(0)
        json.dump(coindata, f, indent=5)


def price():
    grvtprice = coindata('grvt')['quote']['USD']['price']
    return f"${round(grvtprice, 1)}"

def supply():
    grvtsupply = coindata('grvt')['max_supply']
    return grvtsupply

def volume24h():
    grvtvolume = coindata('grvt')['quote']['USD']['volume_24h']
    return grvtvolume

def btcprice():
    btc = coindata('BTC')['quote']['USD']['price']
    grvtbtcprice = coindata('grvt')['quote']['USD']['price'] / btc
    return "{:.15f}".format(grvtbtcprice)

def ethprice():
    eth = coindata('ETH')['quote']['USD']['price']
    grvtethprice = coindata('grvt')['quote']['USD']['price'] / eth
    return "{:.15f}".format(grvtethprice)

def singleprice():
    return "{:.15f}".format(coindata('grvt')['quote']['USD']['price'])

def source():
    return "https://coinmarketcap.com/currencies/gravitoken/"

def data():
    print(coindata('grvt'))

startup()
