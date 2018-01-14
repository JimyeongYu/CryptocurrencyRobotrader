import json
import requests

class coincheck():
    def __init__(self):
        self.baseURL='https://coincheck.com/'

    def getCurrentAskBid(self, productCode):
        self.getTickerURL = self.baseURL + 'api/ticker'
        tickerJSON = requests.get(self.getTickerURL).json()
        minAsk = tickerJSON['ask']
        maxBid = tickerJSON['bid']
        spread = round((minAsk - maxBid) / ((minAsk + maxBid) / 2) * 10000, 2)
        return (minAsk, maxBid, spread)

    def getTransactionHistory(self, productCode):
        self.getTransactionHistoryURL = self.baseURL + 'api/trades'
        transactionHistoryJSON = requests.get(self.getTransactionHistoryURL).json()
        return transactionHistoryJSON

    def getBoardStatus(self, productCode):
        return (None, None)
