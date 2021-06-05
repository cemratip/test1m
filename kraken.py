import urllib.parse
import hashlib
import hmac
import base64
import requests
import json

def get_kraken_signature(urlpath, data, secret):

    postdata = urllib.parse.urlencode(data)
    encoded = (str(data['nonce']) + postdata).encode()
    message = urlpath.encode() + hashlib.sha256(encoded).digest()

    mac = hmac.new(base64.b64decode(secret), message, hashlib.sha512)
    sigdigest = base64.b64encode(mac.digest())
    return sigdigest.decode()

api_sec = "yTiERkyi1xD746de+df5MY/tIsSY/tGgpcMlYTdZ92j+pM3/h0TCFXZG3GL1eYQWbwEUvUw1rkZ8auaNjZa8GQ=="

#data = {
#    "nonce": "1616492376594",
#    "ordertype": "market",
#    "pair": "XBTUSD",
#    #"price": 37500,
#    "type": "buy",
#    "volume": 1.25
#}

#signature = get_kraken_signature("/0/private/AddOrder", data, api_sec)
#print("API-Sign: {}".format(signature))

#kraken public api key: NcYz0XyXRqhONr0Tqc6a9J5JVoNJ4uxwanJjw1KbiyHZMXphhNINRHKN
#kraken private api key: yTiERkyi1xD746de+df5MY/tIsSY/tGgpcMlYTdZ92j+pM3/h0TCFXZG3GL1eYQWbwEUvUw1rkZ8auaNjZa8GQ==

#demo account username: 3jehfb9q@futures-demo.com
#demo account password: l5apkvy7vulcyt1fsj2l

def getmarketprice():
    response = json.loads((requests.get('https://api.kraken.com/0/public/Ticker?pair=XBTUSD')).text)
    marketprice = response['result']['XXBTZUSD']['c'][0]
    print(marketprice)



