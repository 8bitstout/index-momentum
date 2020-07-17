from Nasdaqomx import Nasdaqomx
import yfinance as yf
from datetime import datetime
from dateutil.relativedelta import relativedelta

ndx = Nasdaqomx()
index = 'EMCLOUD'

tickers = ndx.fetchTickers(index)

current_date = datetime.today()
lookback_date = current_date - relativedelta(months=6)

stocks = yf.download(tickers, lookback_date, current_date)
