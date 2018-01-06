import json
import requests

class bitFlyer():
    def __init__(self):
        self.baseURL='https://api.bitflyer.jp/'

    def getCurrentAskBid(self, productCode):
        self.getTickerURL = self.baseURL + 'v1/getticker?product_code=' + productCode
        tickerJSON = requests.get(self.getTickerURL).json()
        minAsk = tickerJSON['best_ask']
        maxBid = tickerJSON['best_bid']
        spread = round((minAsk - maxBid) / ((minAsk + maxBid) / 2) * 10000, 2)
        return (minAsk, maxBid, spread)

    def getTransactionHistory(self, productCode):
        self.getTransactionHistoryURL = self.baseURL + 'v1/getexecutions?product_code=' + productCode
        transactionHistoryJSON = requests.get(self.getTransactionHistoryURL).json()
        return transactionHistoryJSON

    def getBoardStatus(self, productCode):
        self.getBoardStatusURL = self.baseURL + 'v1/getboardstate?product_code=' + productCode
        boardStatusJSON = requests.get(self.getBoardStatusURL).json()
        health = boardStatusJSON['health']
        state = boardStatusJSON['state']
        return (health, state)
