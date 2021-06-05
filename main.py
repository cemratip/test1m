import bitmex, json, time

class Connect:
    def __init__(self, publicapikey, secretapikey):
        global client
        self.publicapikey = publicapikey
        self.secretapikey = secretapikey
        connected = False
        while connected == False:
            client = bitmex.bitmex(test=True, api_key=self.publicapikey, api_secret=self.secretapikey)
            print('Connection established.')
            connected = True

def GetMarketPrice(symbol):
        marketprice = client.Instrument.Instrument_get(filter=json.dumps({'symbol': symbol})).result()
        return marketprice[0][0]["lastPrice"]


class NewOrder:
    def __init__(self, symbol, qty, price):
        self.symbol = symbol
        self.qty = qty
        self.price = price

    def buy(self):
        lastbuy = client.Order.Order_new(symbol=self.symbol, orderQty=self.qty, price=self.price).result()
        print(('Bought {qty} contracts @ ${price}.').format(qty=self.qty, price=self.price))

    def sell(self):
        lastsell = client.Order.Order_new(symbol=self.symbol, orderQty=self.qty*-1, price=self.price).result()
        print(('Sold {qty} contracts @ ${price}.').format(qty=self.qty, price=self.price))


Bitmex = Connect('dFxV0ofVnOXgZhVIpcxFJvWQ', 'ItK9Cz-tpJ10iXENezVANVQkbIuwGwt8CZlT0TvAhTo87IFQ')
qty = 10
NewTrade = NewOrder('XBTUSD', qty, GetMarketPrice('XBTUSD'))
NewTrade.buy()
time.sleep(120)
NewTrade = NewOrder('XBTUSD', qty, GetMarketPrice('XBTUSD'))
NewTrade.sell()

#next time: implement a Market order instead of a Limit order

