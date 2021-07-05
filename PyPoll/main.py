import os
import csv

csvpath = os.path.join("02-Homework/python-challenge/PyPoll/Resources/election_data.csv")
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")
    csvreader = next(csv_reader, None)

ids = []
county = []
candidate = []

for row in csvreader:
    ids.append(row[0])
    county.append(row[1])
    candidate.append(row[2])
