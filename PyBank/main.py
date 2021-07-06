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
        total_am += float(net)

    for i in range(int(len(p_l)-1)):
        change.append(int(p_l[i+1]) - int(p_l[i]))
        
    mon_change = float(sum(change)/months)
    changeformat = "{:.2f}".format(mon_change)
    
max_change = max(change)
min_change = min(change)
maxpos = change.index(max(change))
minpos = change.index(min(change))
maxmonth = dates[maxpos+1]
minmonth = dates[minpos+1]


outputpath = os.path.join("02-Homework/python-challenge/PyBank/analysis/analysis.txt")
with open(outputpath, "w") as file:
    filewriter = file.write("Financial Analysis\n")
    filewriter = file.write("--------------------\n")
    filewriter = file.write("Total Months: " + str(months)+ "\n")
    filewriter = file.write("Total: $" + str(total_am)+ "\n")
    filewriter = file.write("Average Change: $" + str(changeformat)+ "\n")
    filewriter = file.write("Greatest Increase in Profits: " + str(maxmonth) + " ($" + str(max_change) +")\n")
    filewriter = file.write("Greatest Decrease in Profits: " + str(minmonth) + " ($" + str(min_change) + ")\n")


print("Financial Analysis")
print("-------------------")
print("Total Months: " + str(months))
print("Total: $" + str(total_am))
print("Average Change: $" + str(changeformat))
print("Greatest Increase in Profits: " + str(maxmonth) + " ($" + str(max_change) +")")
print("Greatest Decrease in Profits: " + str(minmonth) + " ($" + str(min_change) + ")")

    

