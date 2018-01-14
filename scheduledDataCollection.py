import sched
import time
from datetime import datetime
from exchange.bitFlyer import bitFlyer
from exchange.coincheck import coincheck
from exchange.quoine import quoine
from exchange.Zaif import Zaif
import csv
import os.path
import sys

def getPrice(exchangeObject, productCode):
    (ask, bid, spread) = exchangeObject.getCurrentAskBid(productCode)
    (health, state) = exchangeObject.getBoardStatus(productCode)
    now = datetime.now()
    saveToCSV(fileName, now, ask, bid, spread, health, state)
    print('EVENT:' + str(now) + ' ' + exchangeObject.__class__.__name__ + ' ' + productCode + ' Ask=' + str(ask) + ' Bid = ' + str(bid) + ' spread = ' + str(spread) +'bps')

def saveToCSV(fileName, time, ask, bid, spread, health, state):
    marketHistoryFile = open(fileName, 'a')
    csvwriter = csv.writer(marketHistoryFile, lineterminator='\n')
    csvwriter.writerow([time, ask, bid, (ask+bid)/2, spread, health, state])
    marketHistoryFile.close()

def initializeCSV(fileName):
    CSVFile = open(fileName, 'w')
    csvwriter = csv.writer(CSVFile, lineterminator='\n')
    header = ['timestamp', 'ask', 'bid', 'mid', 'spread', 'health', 'state']
    csvwriter.writerow(header)
    CSVFile.close()

print('取引所名を入力してください。(bitFlyer, coincheck, quoine or Zaif)')
exchange_name = input('>> ')

if exchange_name == 'bitFlyer':
    exchangeObject = bitFlyer()
    fileName = 'marketHistory_bitFlyer.csv'
elif exchange_name == 'coincheck':
    exchangeObject = coincheck()
    fileName = 'marketHistory_coincheck.csv'
elif exchange_name == 'quoine':
    exchangeObject = quoine()
    fileName = 'marketHistory_quoine.csv'
elif exchange_name == 'Zaif':
    exchangeObject = Zaif()
    fileName = 'marketHistory_Zaif.csv'
else:
    print('Unexpected String:' + str(datetime.now()))
    sys.exit()

productCode = 'BTC_JPY'
endDatetime = datetime(2020, 12, 31, 23, 59)

if os.path.exists(fileName) == False:
    initializeCSV(fileName)
print('START:' + str(datetime.now()))

scheduler = sched.scheduler(time.time, time.sleep)
now = datetime.now()
nextScheduleDatetime = datetime(now.year, now.month, now.day, now.hour, now.minute+1)
nextSchedule = int(time.mktime(nextScheduleDatetime.timetuple()))
while now < endDatetime:
    if nextSchedule < int(time.mktime(now.timetuple())):
        scheduler.enterabs(nextSchedule, 1, getPrice, (exchangeObject, productCode))
        nextSchedule += 60
        scheduler.run()
    time.sleep(0.1)
    now = datetime.now()
print('END:' + str(datetime.now()))
