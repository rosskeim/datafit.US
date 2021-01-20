import pandas as pd
import datetime as datetime
import mysql.connector
import sys

"""
Goal: Display Current Weekly Set Totals

- use DataFrames to query the data
- load from SQL table
- display weekly sum for each bodypart:
  > need to account for date
  > if date > x, if date < x
  > x will have to be calculated from
  > ...today's date
  > time library needed
"""

cnx = mysql.connector.connect(host='localhost',
  user='root',
  password='vCAeoLUzYvYH8Ckb',
  database='training')

cursor = cnx.cursor()
df = pd.read_sql('SELECT * FROM training_log;', cnx)

start = datetime.datetime(2020, 12, 28)
end = datetime.datetime(2021, 1, 3)
mask = (df['date'] > start) & (df['date'] <= end)
df = df.loc[mask]

print(df)

quad = (df.bpart == 'quad').sum()
ham = (df.bpart == 'ham').sum()
tricep = (df.bpart == 'tricep').sum()
rsdelt = (df.bpart == 'rsdelt').sum()
back = (df.bpart == 'back').sum()
bicep = (df.bpart == 'bicep').sum()

print("#### WEEK'S RESULTS ####")
print("Quad: " + str(quad))
print("Ham: " + str(ham))
print("Tricep: " + str(tricep))
print("RSDelt: " + str(rsdelt))
print("Back: " + str(back))
print("Bicep: " + str(bicep))
