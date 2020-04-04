# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 06:48:25 2020

@author: JEREMY2852
"""

#Help a small, rural town modernize its vote-counting process.
#CSV file has 3 columns:  `Voter ID`, `County`, and `Candidate`
#Script will produce analysis of this data set

#import the OS module
import os
# module for reading csv files
import csv

#Step 1:  Set the path for the file
polldata_csv = os.path.join("..", "PyPoll", "election_data.csv")


#1. THE TOTAL NUMBER OF VOTES CAST

#open and read the csv file
with open(polldata_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
   
    # Read the header row first so it is not copied into the data lists
    csv_header = next(csvfile)
 
    row_count = sum(1 for row in csvreader)
    
#2. A COMPLETE LIST OF CANDIDATES WHO RECEIVED VOTES
    
#open and read the csv file
with open(polldata_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
   
    # Read the header row first so it is not copied into the data lists
    csv_header = next(csvfile)
    
    #Find the unique values in the Candidate column
    candidates = []
    for row in csvreader:
        if row[2] not in candidates:
            candidates.append(row[2])         
    
#3. THE TOTAL NUMBER OF VOTES EACH CANDIDATE WON
    
#open and read the csv file
with open(polldata_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
   
    # Read the header row first so it is not copied into the data lists
    csv_header = next(csvfile)
    
    count_Khan = 0
    count_Correy = 0
    count_Li = 0
    count_OTooley = 0
    
    for row in csvreader:
        if row[2] == "Khan":
            count_Khan += 1
        elif row[2] == "Correy":
            count_Correy +=1
        elif row[2] == "Li":
            count_Li += 1
        elif row[2] == "O'Tooley":
            count_OTooley += 1
        
#4. THE PERCENTAGE OF VOTES EACH CANDIDATE WON

percent_Khan = format(int(count_Khan) / int(row_count),".3%")
percent_Correy = format(int(count_Correy) / int(row_count),".3%") 
percent_Li = format(int(count_Li) / int(row_count), ".3%") 
percent_OTooley = format(int(count_OTooley) / int(row_count),".3%") 

#5. THE WINNER OF THE ELECTION BASED ON POPULAR VOTE

results = [count_Khan, count_Correy, count_Li, count_OTooley]
index_winner = results.index(max(results))
winner = candidates[index_winner]        

percentages = [percent_Khan, percent_Correy, percent_Li, percent_OTooley]

#6. PRINT THE SUMMARY TABLE

print('Election Results')
print("---------------------")
print('Total Votes:', row_count)
print("---------------------")
print(f"{candidates[0]}: {percentages[0]} ({results[0]})")
print(f"{candidates[1]}: {percentages[1]} ({results[1]})")
print(f"{candidates[2]}: {percentages[2]} ({results[2]})")
print(f"{candidates[3]}: {percentages[3]} ({results[3]})")
print("---------------------")
print(f"Winner:  {winner}")
print("---------------------")

stringa = "Total Votes: " + str(row_count) + ("\n")
stringb = str(candidates[0]) + "  " + str(percentages[0]) + "  (" + str(results[0]) + ")" + ("\n")
stringc = str(candidates[1]) + "  " + str(percentages[1]) + "  (" + str(results[1]) + ")" + ("\n")
stringd = str(candidates[2]) + "  " + str(percentages[2]) + "  (" + str(results[2]) + ")" + ("\n")
stringe = str(candidates[3]) + "  " + str(percentages[3]) + "  (" + str(results[3]) + ")" + ("\n")

stringf = str("Winner:  " + str(winner) + "\n")

#7. EXPORT RESULTS TO A TEXT FILE

output_file = os.path.join("..", "PyPoll", "pypoll_output.txt")
with open(r"output_file","w+") as f:
    f.write("Election Results \n")
    f.write("--------------------- \n")
    f.write(stringa)
    f.write("---------------------\n")
    f.write(stringb)
    f.write(stringc)
    f.write(stringd)
    f.write(stringe)
    f.write("--------------------- \n")
    f.write(stringf)
    f.write("--------------------- \n")
    
f.close()






