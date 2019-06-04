import os
import csv

# path to data file
budget_data_csv = os.path.join('election_data.csv')

#variables
total_votes = 0
candidates_unique = []
candidate_vote_count = []

#read the csv file
with open(budget_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        #This is the total votes cast, just count rows
        total_votes += 1
        #read in the candidate from column 3 of csv
        candidate_in = (row[2])
        #if candidate alreaady in list then locate the candidate by index # and increment the vote count by 1
        if candidate_in in candidates_unique:
            candidate_index = candidates_unique.index(candidate_in)
            candidate_vote_count[candidate_index] = candidate_vote_count[candidate_index] + 1
        else:
            #if candidate was not found in candidates_unique list then append to list and add 1 to vote count
            candidates_unique.append(candidate_in)
            candidate_vote_count.append(1)

#----------------------------------------------------

pct = []
max_votes = candidate_vote_count[0]
max_index = 0

for x in range(len(candidates_unique)):
    #calculation to get the percentage, x is the looper value
    vote_pct = round(candidate_vote_count[x]/total_votes*100, 2)
    pct.append(vote_pct)
    
    if candidate_vote_count[x] > max_votes:
        max_votes = candidate_vote_count[x]
        max_index = x

election_winner = candidates_unique[max_index] 

#----------------------------------------------------
#QA the variables
#print(f'Vote count for each candidate: {candidate_vote_count}')
#print(f'Max votes: {max_votes}')
#print(f'Election winner: {election_winner}')
#----------------------------------------------------

#To terminal
print('======================================================')
print('|                  Election Results                  |')
print('======================================================')
print(f'Total Votes: {total_votes}')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
for x in range(len(candidates_unique)):
    print(f'{candidates_unique[x]} : {pct[x]}% ({candidate_vote_count[x]})')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(f'Election winner: {election_winner.upper()}')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')


#output txt file
output_file = os.path.join("pypoll_election_results.txt")
with open(output_file, "w", newline="") as datafile:
    datafile.write('======================================================\n')
    datafile.write('|                  Election Results                  |\n')
    datafile.write('======================================================\n')
    datafile.write(f'Total Votes: {total_votes}\n')
    datafile.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    for x in range(len(candidates_unique)):
        datafile.write(f'{candidates_unique[x]} : {pct[x]}% ({candidate_vote_count[x]})\n')
    datafile.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    datafile.write(f'Election winner: {election_winner.upper()}\n')
    datafile.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    datafile.write("---END OF REPORT---")
