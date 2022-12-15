'''
Construct a (relational) database with normalized tables & insert both the data files into it
'''

import pandas as pd

file1 = pd.read_csv('Securities available for Equity segment.csv')
file2 = pd.read_csv('Latest Bhav Copy.csv')

# Since only the column 'SYMBOL' is common between both the files,
# we will use it to merge files upon

merged_file = pd.merge(file1, file2, on='SYMBOL')
# upon mergind we found some redundant columns that need to be dropped first before saving the csv file
merged_file.drop("Unnamed: 0_x",inplace=True,axis=1)
merged_file.drop("Unnamed: 0_y",inplace=True,axis=1)
merged_file.drop("Unnamed: 13",inplace=True,axis=1)
merged_file_csv = merged_file.to_csv('Merged File.csv')
