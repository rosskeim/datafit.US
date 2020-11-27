#this script will be to upload the CSV file from
#rep counter export
#
#
#
# database: training
#
# tables:
# - training_log
# - exercise_db
# - plan
#
#
# training_log: the relevant data loaded from the repcounter export
# exercise_db: a colldection of exercises and relevant associated data
# plan: a specified set of exercises as part of planning a training period
#
#
# training_log:
# - date (datetime)
# - exercise (text)
# - weight (double)
# - reps (int)
# - notes (text)
#
#
# exercise_db:
# - id (int) primary key
# - name
# - bpart 
#
#
# plan:
# - date (datetime)
# - id (int)
# - weight (double)
# - reps (int)
# - rir (int)
#
#
# open file stream
# parse through stream (2 options):
# A: establish mysql connection, parse through file
# 	and enter row by row
# B: parse through file into data structure, then load data structure
# 	into SQL INSERT

import mysql.connector
import csv
import sys

cnx = mysql.connector.connect(host='localhost',
				user='root',
				password='vCAeoLUzYvYH8Ckb',
				database='training')

cursor = cnx.cursor()
cursor.execute('SELECT * FROM exercise_db;')
data = cursor.fetchall()
ex_dict = {}
bpart_dict = {}
for row in data:
	ex_dict[row[1]] = row[0]

for row2 in data:
	bpart_dict[row[0]] = row[2]

session_data = []

with open(str(sys.argv[1])) as f:
	reader = csv.DictReader(f) 

	for row in reader:
		date = row['Date']
		name = row['Exercise']
		weight = row['Weight']
		reps = row['Reps']
		notes = row['Notes']
		exid = ex_dict.get(name)
		if(exid is not None):
			bpart = bpart_dict[exid]
			session_data.append([date, exid, weight, reps, notes, bpart])

query = 'INSERT INTO training_log(date, exid, weight, reps, notes, bpart) VALUES (%s,%s,%s,%s,%s,%s)'

for entry in session_data:
	cursor.execute(query, entry)
	cnx.commit()

cursor.close()
cnx.close()

