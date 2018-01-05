from exchange.bitFlyer import bitFlyer
import json
import csv

product_code = 'BTC_JPY'
exchange = bitFlyer(product_code)
transactionHistory = exchange.getTransactionHistory()

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
