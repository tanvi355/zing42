'''
Programatically get the latest “bhavcopy” csv file from the following URL -
https://www.nseindia.com/all-reports
'''

# url format
# https://archives.nseindia.com/content/historical/EQUITIES/{year}/{month}/cm{day}{month}{year}bhav.csv.zip

import datetime
from datetime import date, datetime
import pandas as pd

# function to get the month name
def get_month(m):
    if(m == 1):
        month = "JAN"
    if(m == 2):
        month = "FEB"
    if(m == 3):
        month = "MAR"
    if(m == 4):
        month = "APR"
    if(m == 5):
        month = "MAY"
    if(m == 6):
        month = "JUN"
    if(m == 7):
        month = "JUL"
    if(m == 8):
        month = "AUG"
    if(m == 9):
        month = "SEP"
    if(m == 10):
        month = "OCT"
    if(m == 11):
        month = "NOV"
    if(m == 12):
        month = "DEC"
    return month


# today's date (yyyy-mm-dd) format by default
today_date = str(date.today()).split('-')
# result -> ['2022', '12', '15']
year = today_date[0]
month = get_month(int(today_date[1]))
day = int(today_date[2])

# url format for the latest Bhav copy csv
url = 'https://archives.nseindia.com/content/historical/EQUITIES/2022/'+f"{month}"+'/cm'+f"{day}{month}{year}"+'bhav.csv.zip'
df = pd.read_csv(url)
df.to_csv('Latest Bhav Copy.csv')
