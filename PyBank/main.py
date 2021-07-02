import os
import csv

csv_reader = csv.DictReader(open("Resources","budget_data.csv"))

months = 0
total_pl = 0
avg_pl = 0
great_inc = 0
great_dec = 0
alldat = 0

for row in csv_reader:
    months += 1
    alldat += float(row["Profit/Losses"])
    total_pl += alldat



