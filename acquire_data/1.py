'''
Programatically fetch “Securities available for Equity segment (.csv)” file From the URL:
https://www.nseindia.com/market-data/securities-available-for-trading
'''

import pandas as pd

url= 'https://archives.nseindia.com/content/equities/EQUITY_L.csv'
df = pd.read_csv(url)
df.to_csv('Securities available for Equity segment.csv')
