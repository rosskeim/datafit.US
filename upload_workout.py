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
row = cursor.fetchone()
ex_dict = {}
while row is not None:
	print('inside while')
	row = cursor.fetchone()
	ex_dict[row[1]] = row[0]

print(ex_dict)

#cursor.close()
#session_data = []

#with open(sys.argv[0]) as f:
	#reader = csv.reader(f) 

	#for frow in reader:
		#print(frow)
		#date = row[0]
		#name = row[1]
		#weight = row[2]
		#reps = row[3]
		#notes = row[4]
		#exid = ex_dict.get(name)
		#if(exid is not None):
		#	session_data.append(date, exid, weight, reps, notes)

#query = 'INSERT INTO training_log(date, exid, weight, reps, notes) \
#	VALUES (%s,%s,%s,%s,%s)'

#cursor = cnx.cursor()

#cursor.executemany(query, session_data)
#cursor.close()
#cnx.close()

