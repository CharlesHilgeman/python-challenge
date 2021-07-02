import os
import csv

csvpath = os.path.join("02-Homework/python-challenge/PyBank/Resources/budget_data.csv")
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")

    p_l = []
    for row in csv_reader:
        p_l.append(row[1])
        
    months = 0
    for months in p_l:
        months += 1

        


    

