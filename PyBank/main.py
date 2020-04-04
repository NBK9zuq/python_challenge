#import the OS module
import os
# module for reading csv files
import csv
# module for converting dates
import datetime


# set the path for the file
budget_csv = os.path.join("..", "PyBank", "budget_data.csv")

# create lists to store data
dates = []
profits = []
profitchgs = []


#open and read the csv file
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
   
    # Read the header row first so it is not copied into the data lists
    csv_header = next(csvfile)
    
    #create a group of lists made up of profit/loss data
    #loop through rows in the csv file to build the data lists
    for row in csvreader:
        # create the date list from row position 0
        dates.append(row[0])
        # create the profits list from row position 1 
        profits.append(int(row[1]))

# create the list to hold the changes in profits
x = 0
while x < len(profits) - 1:
    profitchg = profits[x + 1] - profits[x]
    profitchgs.append(profitchg)
    x += 1

#calculations for print statements to include in analysis

index_greatest = profitchgs.index(max(profitchgs))+1
date_greatest = dates[index_greatest]

index_lowest = profitchgs.index(min(profitchgs))+1
date_lowest = dates[index_lowest]

#Print analysis summary
print("Financial Analysis")
print("---------------------")
print("Total Months:", len(profits))
print("Total:", "$",sum(profits))
print("Average Change:", "$", "%.2f" % (sum(profitchgs) / len(profitchgs))) 
print("Greatest Increase in profits:", dates[index_greatest], "($", max(profitchgs), ")")
print("Greatest Decrease in profits:", dates[index_lowest], "($", min(profitchgs), ")")



        
        
        
        