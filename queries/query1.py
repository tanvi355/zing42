import pandas as pd
import sqlite3

print('***Top 25 gainers of the day sorted in the order of their gains:***\n')

# read the data
data = pd.read_csv('Merged File.csv')

# create the database connection object
conn = sqlite3.connect('nse_database.db')
# write records stored in dataframe to SQL database
data.to_sql('nse_data_table', conn, if_exists='append', index=False)

# gain formula = ((close-open)/open)
# perform the query
cur = conn.cursor()
cur.execute('''SELECT DISTINCT `NAME OF COMPANY`, ((CLOSE-OPEN)/(OPEN)) AS GAIN FROM nse_data_table ORDER BY (GAIN) DESC limit 25''')
output = cur.fetchall()
for row in output:
    print(row)

conn.commit()
conn.close()
