#PyPoll Challenge

import os
import csv

#variables
total_votes = []
candidates = []
candidates_individuals = []
candidates_votes = []


# Path to collect data from the Resources folder
election_data_csv = os.path.join('Resources', 'election_data.csv')


# Read in the CSV file
with open(election_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    for row in csvreader:  
        ballot_ids = row[0]
        total_votes.append(ballot_ids)
        each_candidate = row[2]
        candidates.append(each_candidate)
#print(len(total_votes)) => 369711   

candidates_individuals.append(candidates[0])  
count_of_votes = len(total_votes)      
for i in range (count_of_votes-1):  
    if candidates[i+1] not in candidates_individuals:
            candidates_individuals.append(candidates[i+1])
#print(candidates_individuals) => ['Charles Casper Stockham', 'Diana DeGette', 'Raymon Anthony Doane']

count_of_candidates = len(candidates_individuals)
for j in range (count_of_candidates):
    candidates_votes.append(candidates.count(candidates_individuals[j]))
#print(candidates_votes) => [85213, 272892, 11606]


votes_per_candidate = {candidates_individuals[r]:candidates_votes[r] for r in range(len(candidates_individuals))}

#print(votes_per_candidate) ==> {'Charles Casper Stockham': 85213, 'Diana DeGette': 272892, 'Raymon Anthony Doane': 11606}

winner = max(votes_per_candidate, key=votes_per_candidate.get)
#print(winner) ==> Diana DeGette

percentage_of_vote_1 = candidates_votes[0] / len(total_votes)*100
#print(percentage_of_vote_1)
percentage_of_vote_2 = candidates_votes[1] / len(total_votes)*100
percentage_of_vote_3 = candidates_votes[2] / len(total_votes)*100


# Print the results
print("Election Results")
print("-----------------------")
print(f"Total Votes: " + str(len(total_votes)))
print("-----------------------")
print(f"{candidates_individuals[0]}: {round(percentage_of_vote_1, 3)}% ({candidates_votes[0]})")
print(f"{candidates_individuals[1]}: {round(percentage_of_vote_2, 3)}% ({candidates_votes[1]})")
print(f"{candidates_individuals[2]}: {round(percentage_of_vote_3, 3)}% ({candidates_votes[1]})")
print("-----------------------")
print(f"Winner: " + winner)
print("-----------------------")


#Exporting the results to a text

Results_txt = os.path.join('analysis', 'Results.txt')

lines = ["Election Results","-----------------------",f"Total Votes: " + str(len(total_votes)),"-----------------------",
          f"{candidates_individuals[0]}: {round(percentage_of_vote_1, 3)}% ({candidates_votes[0]})",
          f"{candidates_individuals[1]}: {round(percentage_of_vote_2, 3)}% ({candidates_votes[1]})",
          f"{candidates_individuals[2]}: {round(percentage_of_vote_3, 3)}% ({candidates_votes[2]})",
          "-----------------------",f"Winner: " + winner,"-----------------------"]

with open(Results_txt, "w") as f:
    for line in lines:
        f.write(line)
        f.write("\n")
        f.write("\n")          