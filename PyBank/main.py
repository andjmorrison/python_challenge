#budget script

#import modules
import os
import csv

#path to collect from--same folder
banking_csv = os.path.join('budget_data.csv')

#--------------------

#lists
bankingData = []
#month list/variable
monthData = []
num_months = 0
#net list/variable
netData = []
net_total = 0
#change list/variable
changeData = []
changeValues = []
change_total = 0

#increase list/decrease list
increaseData = []
decreaseData = []

#--------------------

#open file, 'read'
with open(banking_csv, 'r') as csvfile:
    
    #create csvreader object
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip header row
    next(csvreader)

    #for loop, rows
    for row in csvreader:

        #add months rows to list 
        monthData.append(row[0])

        #add profit rows to list
        netData.append(int(row[1]))
        
        #add profit rows to new list
        changeData.append(round(int(row[1]),2))

#--------------------

#take length of months list to get total months
num_months = len(monthData)

#add up net totals cumulatively
for i in netData:
    net_total += i

#list comprehension for change b/w each month
changeValues = [j-i for i,j in zip(changeData, changeData[1:])]

#add up each value cumulatively
for i in changeValues:
    change_total += i

#value total divided by month total less starting month, rounded for currency 
#(import a special money module for future currency manipulation?)
change_final = round((change_total/(num_months-1)),2)

#calculate largest monthly increase
increaseData = max(changeValues)

#calculate largest monthly decrease
decreaseData = min(changeValues)

#--------------------

#print results
print(f"""
Financial Analysis:
--------------------
Total Months: {num_months}
Net Total: ${net_total}
Average Change: ${change_final}
Greatest Increase in Profits: ${increaseData} 
Greatest Decrease in Profits: ${decreaseData}
""")

#--------------------

#create txt file
results_txt = os.path.join("budget_data_results.txt")

#write txt file (string is properly formatted--if indented 102-107 text indents in file)
with open(results_txt, 'w') as newfile:

    newfile.write(f"""Financial Analysis:
--------------------
Total Months: {num_months}
Net Total: ${net_total}
Average Change: ${change_final}
Greatest Increase in Profits: ${increaseData} 
Greatest Decrease in Profits: ${decreaseData}""")