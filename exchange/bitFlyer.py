import json
import requests

class bitFlyer():
    def __init__(self, product_code):
        self.baseURL='https://api.bitflyer.jp/'
        self.product_code = product_code

    def getCurrentAskBid(self):
        self.getBoardURL = self.baseURL + 'v1/getboard?product_code=' + self.product_code
        boardJSON = requests.get(self.getBoardURL).json()
        maxBid = boardJSON['bids'][0]['price']
        minAsk = boardJSON['asks'][0]['price']
        return (maxBid, minAsk)

    def getTransactionHistory(self):
        self.getTransactionHistoryURL = self.baseURL + 'v1/getexecutions?product_code=' + self.product_code
        TransactionHistoryJSON = requests.get(self.getTransactionHistoryURL).json()
        return TransactionHistoryJSON
