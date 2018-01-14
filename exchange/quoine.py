import json
import requests

class quoine():
    def __init__(self):
        self.baseURL='https://api.quoine.com/'

    def getCurrentAskBid(self, productCode):
        self.getTickerURL = self.baseURL + 'products/code/CASH/' + productCode[0:3].upper() + productCode[4:7].upper()
        tickerJSON = requests.get(self.getTickerURL).json()
        minAsk = tickerJSON['market_ask']
        maxBid = tickerJSON['market_bid']
        spread = round((minAsk - maxBid) / ((minAsk + maxBid) / 2) * 10000, 2)
        return (minAsk, maxBid, spread)

    def getTransactionHistory(self, productCode):
        return None

    def getBoardStatus(self, productCode):
        return (None, None)
