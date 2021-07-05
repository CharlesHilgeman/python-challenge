import os
import csv

csvpath = os.path.join("02-Homework/python-challenge/PyBank/Resources/budget_data.csv")
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ",")
    csvreader = next(csv_reader, None)
    
    p_l = []
    change = []
    dates = []

    for row in csv_reader:
        dates.append(row[0])
        p_l.append(row[1])
        
    months = 0
    for month in dates:
        months += 1

    total_am = 0
    for net in p_l:
        total_am += int(net)

    mon_change = 0
    for i in range(1,len(p_l)-1):
        change.append(int(p_l[i+1]) - int(p_l[i]))
        
    mon_change = sum(change)/months

    max_change = max(p_l)
    min_change = min(p_l)
    maxpos = p_l.index(max(p_l))
    minpos = p_l.index(min(p_l))
    maxmonth = dates[maxpos]
    minmonth = dates[minpos]


    

    print("Financial Analysis")
    print("-------------------")
    print("Total Months: " + str(months))
    print("Total: $" + str(total_am))
    print("Average Change: $" + str(mon_change))
    print("Greatest Increase in Profits: " + str(maxmonth) + " ($" + str(max_change) +")")
    print("Greatest Decrease in Profits: " + str(minmonth) + " ($" + str(min_change) + ")")


    

