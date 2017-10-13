#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from api import BinanceAPI


API_KEY = b'xxx'
API_SECRET = b'xxx'



def public_api():

    client = BinanceAPI()

    print(client.ping())

    print(client.time())
    
    print(client.depth('BTCUSDT', limit=10))
    
    print(client.aggTrades('ETHBTC'))
    
    print(client.klines('BNBBTC', '1h', limit=10))
    
    print(client.stats24hr('ETHUSDT'))
    
    print(client.allPrices())
    
    print(client.allBookTickers())


def private_api():

    client = BinanceAPI(API_KEY, API_SECRET)
    # or 
    # client = BinanceAPI()
    # client.set_api(API_KEY, API_SECRET)

    print(client.openOrders('KNCETH'))

    print(client.allOrders('KNCETH'))
    
    print(client.account())
    
    print(client.myTrades('KNCETH'))

    print(client.newLimitBuyOrder('BTCUSDT', quantity=1.0, price=5203.0))

    print(client.queryOrder('BNBETH', orderId=387643))

    print(client.deleteOrder('BNBETH', orderId=387643))
