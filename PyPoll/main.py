import os
import csv

csvpath = os.path.join("02-Homework/python-challenge/PyPoll/Resources/election_data.csv")
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")
    csvreader = next(csv_reader, None)