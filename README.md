# python-challenge

This project was a demo on how to conduct bigger data using python. I constructed these scripts to better analyze polling and budget data to come up with heplful statistics.


PyBank
Iterating through this allowed me to get a better picture of how budgeting fared through the course of the sample data.
I was able to open the file path as well as the file using "os" and "csv" functions and left the header for better usability.
I created lists to be able to append the data into my code.
Iterating through again, I was able to determine how many months are in the csv and the total amount of money.
From there, I was able to create another list and append data for the average change in profit/loss per month.
I used built in functions "max()" and "min()" to determine the highest and lowest months and indexed them to attach the month in the list I created at the start.
Using concatenation, I was able to dim all of my data into strings to be able to print and export.
Finally, at the end I used the open and write to export my findings to a .txt file as well as print it to the terminal below producing the output I wanted.


PyPoll
Iterating through this data enabled me to determmine election data of a sample poll.
I was able to determine vote counts, vote percentages, total votes, and the winner.
Similarly, I was able to open the file path as well as the file using "os" and "csv" functions and left the header for better usability. I created lists to be able to append the data into my code.
I used a simple for loop to be able to tally total voters through the first column.
To calculate the vote total for each candidate, I set up another for loop and created if statements to add a vote when each candidate name appeared in the data.
Using simple mathematical statements from that data, I found the percent of the vote each candidate received and used formatting syntax for better readability in my output.
From there, I created two more lists with the candidate names and the votes they received.
Using the max function, I was able to index that value to print the candidate with the corresponding vote count.
Finally, at the end I used the open and write to export my findings to a .txt file as well as print it to the terminal below producing the output I wanted.

