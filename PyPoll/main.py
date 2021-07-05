import os
import csv

csvpath = os.path.join("02-Homework/python-challenge/PyPoll/Resources/election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheader = next(csvreader, None)

    ident = []
    county = []
    candidate = []

    for row in csvreader:
        ident.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

    voters = 0
    for id in ident:
        voters += 1


print(str(voters))


