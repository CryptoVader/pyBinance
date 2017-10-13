pyBinance Python API
========

This is a Python wrapper for `Binance <https://www.binance.com/restapipub.html>`_.

Installation
------------

``pybinance`` is available on `PYPI <https://pypi.python.org/pypi/pybinance/>`_.
Install with ``pip``:

.. code:: bash

    pip install pybinance

Documentation
-------------

First, you need to `register with Binance <https://binance.com>`_.

Then, you need to `create an API Key  <https://www.binance.com/userCenter/createApi.html>`_.

Examples: usage of the public API
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    from binance.api import BinanceAPI
    client = BinanceAPI()


**Check the server is online**

.. code:: python

    client.ping()


**Get the server time**

.. code:: python

    client.time()


**Get the order book**

.. code:: python

    client.depth('BTCUSDT', limit=10)


**Get compressed, aggregate trades**

.. code:: python

    client.aggTrades('ETHBTC')


**Get the Kline/candlestick bars for a symbol**

.. code:: python

    client.klines('BNBBTC', '1h', limit=10)


**Get the 24 hour price change statistics**

.. code:: python

    client.stats24hr('ETHUSDT')


**Latest price for all symbols.**

.. code:: python

    client.allPrices()


**Best price/qty on the order book for all symbols.**

.. code:: python

    client.allBookTickers()


Usage of the private API
^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    client = BinanceAPI(API_KEY, API_SECRET)
    # or 
    # client = BinanceAPI()
    # client.set_api(API_KEY, API_SECRET)


**Send a new LIMIT BUY order**

.. code:: python

    client.newLimitBuyOrder('BTCUSDT', quantity=1.0, price=5203.0)


**Send a new MARKET SELL order**

.. code:: python

    client.newMarketSellOrder('BTCUSDT', quantity=1.0, price=5203.0)



**Check an order's status.**

.. code:: python

    client.queryOrder('BNBETH', orderId=387643)


**Cancel an active order.**

.. code:: python

    client.deleteOrder('BNBETH', orderId=387643)


**Get all open orders on a symbol.**

.. code:: python

    client.openOrders('KNCETH')


**Get all account orders; active, canceled, or filled.**

.. code:: python

    client.allOrders('KNCETH')


**Get current account information.**

.. code:: python

    client.account()


**Get trades for a specific account and symbol.**

.. code:: python

    client.myTrades('KNCETH')




Changelog
---------


v0.0.1 - 2017-10-12
^^^^^^^^^^^^^^^^^^^

Initial version
