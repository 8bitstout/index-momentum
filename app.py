from Nasdaqomx import Nasdaqomx
import yfinance as yf
from datetime import datetime
from dateutil.relativedelta import relativedelta

def get_my_key(obj):
  return obj['return']

ndx = Nasdaqomx()
index = 'EMCLOUD'

tickers = ndx.fetchTickers(index)

current_date = datetime.today()
lookback_date = current_date - relativedelta(months=6)

stocks = yf.download(tickers, lookback_date, current_date)

multpl_stock_daily_returns = stocks['Adj Close'].pct_change()

stock_returns = []

for stock in stocks['Adj Close']:
  s = stocks['Adj Close'][stock]
  r = ((s[-1] / s[0])-1) * 100
  stock_returns.append({ 'name': s.name, 'return': r })

  
stock_returns.sort(key=get_my_key)
stock_returns.reverse()
print(stock_returns[0:5])