#PyPoll
import os
import csv

with open ("output.txt","w") as homework:

    candidates = {}
    filepath = os.path.join("Resources", "election_data.csv")
    with open (filepath) as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ",")   
        header = next(csvreader)
        for row in csvreader:
            candidate = row[2]
            if candidate in candidates.keys():
                candidates[candidate] += 1
            else:
                candidates[candidate] = 1
    total_votes = sum(candidates.values())
    print("Elections Results")
    homework.writelines("Elections Results\n")
    greatest_votes = 0
    winner = ""
    for key, value in candidates.items():
        vote_percent = round((value/total_votes)*100,2)
        print(f'Candidate: {key}, Percent of Votes: {vote_percent}%, (Votes: {value})')
        homework.writelines(f'Candidate: {key}, Percent of Votes: {vote_percent}%, (Votes: {value})\n')
        if value > greatest_votes:
            greatest_votes = value
            winner = key


    print(f'Total Votes: {total_votes}')
    homework.writelines(f'Total Votes: {total_votes}\n')
    print(f'Winner: {winner}!')
    homework.writelines(f'Winner: {winner}!\n')

