from exchange.bitFlyer import bitFlyer

product_code = 'BTC_JPY'
exchange = bitFlyer(product_code)
(bid, ask) = exchange.getCurrentAskBid()
spread = round((ask - bid) / (ask + bid) * 10000, 2)

print('bid = '+str(bid))
print('ask = '+str(ask))
print('spread = '+str(spread)+' bps')
