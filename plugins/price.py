#coding: utf-8
from lib import bitflyerapi
from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply

@listen_to('/price')
def say_prices(message):
    prices = bitflyerapi.get_prices()
    t = '''BTC/JPY : {0[btc_jpy]}
ETH/BTC : {0[eth_btc]} (ETH/JPY : {0[eth_jpy]})'''.format(prices)
    message.send(t)
