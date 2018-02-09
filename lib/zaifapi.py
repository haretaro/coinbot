#coding: utf-8
#zaif API
#http://techbureau-api-document.readthedocs.io/ja/latest/index.html
from urllib.parse import urljoin
import json
import requests

baseurl = "https://api.zaif.jp/api/1/"

def price(currency):
    return price_pair(currency, 'jpy')

def btcprice(currency):
    return price_pair(currency, 'btc')

def price_pair(currency1, currency2):
    currency1 = currency1.lower()
    currency2 = currency2.lower()
    res = requests.get(urljoin(baseurl, "last_price/{}_{}".format(currency1, currency2)))
    j = json.loads(res.text)
    if 'last_price' in j:
        return j['last_price']
    else:
        return -1
