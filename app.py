from Nasdaqomx import Nasdaqomx

ndx = Nasdaqomx()
index = 'EMCLOUD'

tickers = ndx.fetchTickers(index)

print(tickers)