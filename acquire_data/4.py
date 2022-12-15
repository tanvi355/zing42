'''
In addition to step 2, programmatically get bhavcopies of the last 30 days instead of just the latest one.
'''


from datetime import timedelta
import requests
import pandas as pd


today = datetime.now()
today = today -timedelta(days=1)
today1 = datetime.now()
today1 = today1 - timedelta(days=1)
count = 0
i = 0
while 1:
    yesterday = today1 - timedelta(days=i)
    dt = today - timedelta(days=i)
    i+=1

    x = dt.weekday()
    # print(x)
    yr = str(yesterday.year)
    m = yesterday.month
    month=get_month(m)
    d = '{:02d}'.format(yesterday.day)
    d = str(d)
    if x==5 or x==6:
        continue
    if d=='00':
        continue
    current_date = d+month+yr
    if current_date == '08NOV2022' :
        continue
    if current_date == '26OCT2022' :
        continue
    print(current_date)
    url2 = 'https://archives.nseindia.com/content/historical/EQUITIES/2022/'+f"{month}"+'/cm'+f"{current_date}"+'bhav.csv.zip'
    r = requests.get(url2)

    if r.status_code == 200:

        df = pd.read_csv(url2)
        count+=1
        df.to_csv('bhavcopies'+f"{count}"+'.csv')

    if count ==30:
        break
     
