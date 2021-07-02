import os
import csv

csvpath = os.path.join("Resorces", "03-Python_02-Homework_Instructions_PyBank_Resources_budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")
    print(csvreader)

csvheader = next(csvreader)
print(csvheader)