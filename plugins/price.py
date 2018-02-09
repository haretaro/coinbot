#coding: utf-8
from lib import bitflyerapi
from lib import zaifapi
from slackbot.bot import default_reply
from slackbot.bot import listen_to
from slackbot.bot import respond_to

@listen_to('\$price\s+\S.*')
def say_price(message):
    text = message.body['text']
    _, currency = text.split(None, 1)
    value = zaifapi.price(currency)
    t = '{} {}/JPY'.format(value, currency.upper())
    message.send(t)

@listen_to('\$btcprice\s+\S.*')
def say_price(message):
    text = message.body['text']
    _, currency = text.split(None, 1)
    value = zaifapi.btcprice(currency)
    t = '{} {}/BTC'.format(value, currency.upper())
    message.send(t)

@listen_to('\$bitflyer')
def say_bitflyer_prices(message):
    prices = bitflyerapi.get_prices()
    t = '''bitflyer
BTC/JPY : {0[btc_jpy]}
ETH/BTC : {0[eth_btc]}'''.format(prices)
    message.send(t)

@listen_to('\$help')
def help(message):
    t = '''usage
$price <currency> : <currency>/JPY を表示(zaif)
$btcprice <currency> : <currency>/BTC を表示(zaif)
$bitflyer : bitflyer のBTCとETHの価格を表示'''
    message.send(t)
