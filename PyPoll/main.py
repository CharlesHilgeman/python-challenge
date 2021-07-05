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
    
    khanvote = 0
    correyvote = 0
    livote = 0
    otoolvote = 0

    
    for num in candidate:
        if num == "Khan":
            khanvote += 1
        elif num == "Correy":
            correyvote += 1
        elif num == "Li":
            livote += 1
        else:
            otoolvote += 1
    
    khanperc = (khanvote/voters) *100
    formatkhan = "{:.3f}".format(khanperc)
    correyperc = (correyvote/voters) *100
    formatcorrey = "{:.3f}".format(correyperc)
    liperc = (livote/voters) *100
    formatli = "{:.3f}".format(liperc)
    otoolperc = (otoolvote/voters) *100
    formatotool = "{:.3f}".format(otoolperc)

        

print("Election Results")
print("--------------------")
print("Total Votes: " + str(voters))
print("--------------------")
print("Khan: " + str(formatkhan) + "% (" + str(khanvote)+ ")" )
print("Correy: " + str(formatcorrey) + "% (" + str(correyvote)+ ")" )
print("Li: " + str(formatli) + "% (" + str(livote) + ")" )
print("O'Tooley: " + str(formatotool) + "% (" + str(otoolvote)+ ")" )


