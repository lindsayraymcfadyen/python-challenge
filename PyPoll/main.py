#Import dependencies 
import os
import csv 

#Path
path = os.path.join('python-challenge/PyPoll/resources/election_data.csv')

candidates = {}
total_votes = 0

with open(path, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)
    
    for row in csvreader:
        total_votes += 1
        if row[2] not in candidates:
            candidates[row[2]] = 1
        else:
            candidates[row[2]] += 1

percent_votes = {}
winner = None
max_votes = 0

for candidate, votes in candidates.items():
    percent_votes[candidate] = "{:.3f}%".format((votes / total_votes) * 100)
    if votes > max_votes:
        max_votes = votes
        winner = candidate

#Printing Results 
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")
for candidate, votes in candidates.items():
    print(f"{candidate}: {percent_votes[candidate]} ({votes})")
print("--------------------------")
print(f"Winner: {winner}")
print("--------------------------")

#Export Results
write_path = os.path.join('python-challenge/PyPoll/election_results.txt')
results = []
results.append("Election Results")
results.append("--------------------------")
results.append(f"Total Votes: {total_votes}")
results.append("--------------------------")
for candidate, votes in candidates.items():
    results.append(f"{candidate}: {percent_votes[candidate]} ({votes})")
results.append("--------------------------")
results.append(f"Winner: {winner}")
results.append("--------------------------")

with open(write_path, 'w', encoding='utf-8') as file:
    for line in results:
        file.write(line + '\n')