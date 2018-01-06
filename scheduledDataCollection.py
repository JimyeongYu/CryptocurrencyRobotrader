import sched
import time
from datetime import datetime
from exchange.bitFlyer import bitFlyer
import csv
import os.path

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

productCode = 'BTC_JPY'
exchangeObject = bitFlyer()
endDatetime = datetime(2018, 1, 6, 17, 27)
fileName = 'marketHistory_bitFlyer.csv'
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
