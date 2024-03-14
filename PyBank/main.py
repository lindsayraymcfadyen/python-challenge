#Import dependencies 
import os
import csv

#Creating an object out of the CSV file
path = os.path.join('python-challenge/PyBank/resources/budget_data.csv')

total_months = 0
total_pl = 0
value = 0
change = 0
dates = []
profits = []

#Opening and reading the CSV file
with open(path, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Reading header row
    csv_header = next(csvreader)

    first_row = next(csvreader)
    total_months += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])
    
    for row in csvreader:
        dates.append(row[0])
        
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        #Total number of months
        total_months += 1

        #Total net amount of "Profit/Losses over entire period"
        total_pl = total_pl + int(row[1])

    #Greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    #Greatest decrease (lowest increase) in profits 
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    #Average change in "Profit/Losses between months over entire period"
    avg_change = sum(profits)/len(profits)
    

#Run Code
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_pl)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")


#Export Results 
write_path = os.path.join('python-challenge/PyBank/financial_analysis.txt')
results = []
results.append("Financial Analysis")
results.append("---------------------")
results.append(f"Total Months: {str(total_months)}")
results.append(f"Total: ${str(total_pl)}")
results.append(f"Average Change: ${str(round(avg_change,2))}")
results.append(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
results.append(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

with open(write_path, 'w', encoding='utf-8') as file:
    for line in results:
        file.write(line + '\n')