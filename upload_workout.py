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
