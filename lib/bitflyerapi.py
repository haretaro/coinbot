#coding: utf-8
#BitFlyer API使用
#https://lightning.bitflyer.jp/docs?lang=ja&_ga=2.175741408.351313839.1518157736-1827753726.1517542448
import requests
from urllib.parse import urljoin
import json

baseurl = 'https://lightning.bitflyer.jp'

def get_board(product_code):
    parameter = {'product_code': product_code}
    res = requests.get(urljoin(baseurl, 'v1/getboard'), parameter)
    return res

def get_prices():
    res = get_board('BTC_JPY')
    btc_jpy = float(json.loads(res.text)['mid_price'])
    res = get_board('ETH_BTC')
    eth_btc = float(json.loads(res.text)['mid_price'])
    eth_jpy = eth_btc * btc_jpy
    return {'btc_jpy': btc_jpy, 'eth_btc': eth_btc, 'eth_jpy': eth_jpy}
