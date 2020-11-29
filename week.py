import mysql.connector as sql
import pandas as pd
import matplotlib.pyplot as plt

db_connection = sql.connect(host='localhost', database='training', user='root', password='vCAeoLUzYvYH8Ckb')
db_cursor = db_connection.cursor()
db_cursor.execute('SELECT * FROM training_log')

table_rows = db_cursor.fetchall()

df = pd.DataFrame(table_rows)

df.plot()
plt.figure()
