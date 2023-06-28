#PyBank challenge

import os
import csv

# variables
months = []
changes_profit_loss = []
profit_loss = []

# Path to collect data from the Resources folder
budget_data_csv = os.path.join('Resources', 'budget_data.csv')


# Read in the CSV file
with open(budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    
#Append months, profit_loss and changes_profit_loss    
    for row in csvreader:
        months.append(row[0])
        profit_loss.append(int(row[1]))
    
for i in range(len(profit_loss)-1):
    changes_profit_loss.append((profit_loss[i+1]) - profit_loss[i])
    
#Calculating the highest & lowest changes and the highest & lowest months with the list we just appended
highest_change = max(changes_profit_loss)
lowest_change = min(changes_profit_loss)

highest_month = changes_profit_loss.index(highest_change)+1
lowest_month = changes_profit_loss.index(lowest_change)+1

# Print the results
print("Financial Analysis")
print("------------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(profit_loss)}")
print(f"Average Change: ${round(sum(changes_profit_loss)/len(changes_profit_loss),2)}")
print(f"Greatest Increase in Profits: {months[highest_month]} (${highest_change})")
print(f"Greatest Decrease in Losses: {months[lowest_month]} (${lowest_change})")


#Exporting the results to a text
Results_txt = os.path.join('analysis', 'Results.txt')

lines = ["Financial Analysis", "------------------------------", f"Total Months: {len(months)}",f"Total: ${sum(profit_loss)}",
        f"Average Change: ${round(sum(changes_profit_loss)/len(changes_profit_loss),2)}",f"Greatest Increase in Profits: {months[highest_month]} (${highest_change})",
        f"Greatest Decrease in Losses: {months[lowest_month]} (${lowest_change})"]

with open(Results_txt, "w") as f:
    for line in lines:
        f.write(line)
        f.write("\n")
        f.write("\n")






        








