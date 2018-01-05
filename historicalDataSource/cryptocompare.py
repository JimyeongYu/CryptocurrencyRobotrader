import json
import requests

class cryptocompare():
    def __init__(self, product_code, exchange_name):
        self.URL='https://min-api.cryptocompare.com/data/histominute?fsym='+product_code[0:3]+'&tsym='+product_code[4:7]+'&limit=2000&e='+exchange_name

    def getHistoricalCandlestick(self):
        historicalJSON = requests.get(self.URL).json()
        return historicalJSON
