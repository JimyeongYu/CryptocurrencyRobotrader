import json
import requests

class Zaif():
    def __init__(self):
        self.baseURL='https://api.zaif.jp/api/1/'

    def getCurrentAskBid(self, productCode):
        self.getTickerURL = self.baseURL + 'ticker/' + productCode.lower()
        tickerJSON = requests.get(self.getTickerURL).json()
        minAsk = tickerJSON['ask']
        maxBid = tickerJSON['bid']
        spread = round((minAsk - maxBid) / ((minAsk + maxBid) / 2) * 10000, 2)
        return (minAsk, maxBid, spread)

    def getTransactionHistory(self, productCode):
        return None

    def getBoardStatus(self, productCode):
        return (None, None)
