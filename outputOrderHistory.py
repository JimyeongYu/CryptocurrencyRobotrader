from exchange.bitFlyer import bitFlyer
import json
import csv

productCode = 'BTC_JPY'
exchange = bitFlyer()
transactionHistory = exchange.getTransactionHistory(productCode)

transactionHistoryFile = open('./transactionHistory_bitFlyer.csv', 'w')

csvwriter = csv.writer(transactionHistoryFile)
count = 0
for tr in transactionHistory:
      if count == 0:
             header = tr.keys()
             csvwriter.writerow(header)
             count += 1
      csvwriter.writerow(tr.values())
transactionHistoryFile.close()
