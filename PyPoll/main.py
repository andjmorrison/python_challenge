#polling script

import os
import csv

#define file
election_csv = os.path.join('election_data.csv')

#define variables
voteTotal = []

voteKhan = []
kahnCent = 0

voteCorrey = []
correCent= 0

voteLi = []
liCent = 0

voteTooley = []
toolCent= 0

winner = []

#--------------------

#open file
with open (election_csv, 'r') as csvfile:

    #create csvreader object
    csvreader = csv.reader(csvfile, delimiter= ',')
    
    #skip header
    next(csvreader)
    
    for row in csvreader:
        
        #collect all votes
        voteTotal.append(row[0])
        
        #khan conditional | list append
        if row[2] == "Khan":
            voteKhan.append(row[2])

        #correy conditional | list append
        if row[2] == "Correy":
            voteCorrey.append(row[2])
        
        #li conditional | list append
        if row[2] == "Li":
            voteLi.append(row[2])

        #tooley conditional | list append
        if row[2] == "O'Tooley":
            voteTooley.append(row[2])

#calculate percentages based on total votes
kahnCent = int(round(len(voteKhan)/len(voteTotal),3)*100)
correCent = int(round(len(voteCorrey)/len(voteTotal),3)*100)
liCent = int(round(len(voteLi)/len(voteTotal),3)*100)
toolCent = int(round(len(voteTooley)/len(voteTotal),3)*100)

#calculate winner | new list
winnerVal = [kahnCent, correCent, liCent, toolCent]
winner = max(winnerVal)

#conditional statement | winner
if winner == liCent:
    winner = "Li"
elif winner == correCent:
    winner = "Correy"
elif winner == kahnCent:
    winner = "Kahn"
elif winner == toolCent:
    winner = "O'Tooley"

#--------------------

#results
print (f"""
Election Results Are In!
--------------------
Total Votes: {len(voteTotal)}
--------------------
Kahn: {kahnCent}% ({len(voteKhan)})
Correy: {correCent}% ({len(voteCorrey)})
Li: {liCent}% ({len(voteLi)})
Tooley: {toolCent}% ({len(voteTooley)})
--------------------
Congratulations to the winner: {winner}!
""")

#output file

poll_output = os.path.join ('poll_output.txt')

with open (poll_output, 'w') as textfile:
    textfile.write(f"""
Election Results
--------------------
Total Votes: {len(voteTotal)}
--------------------
Kahn: {kahnCent}% ({len(voteKhan)})
Correy: {correCent}% ({len(voteCorrey)})
Li: {liCent}% ({len(voteLi)})
Tooley: {toolCent}% ({len(voteTooley)})
--------------------
Winner: {winner}
""")
