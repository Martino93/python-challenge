# PyPoll Python Challenge
import csv
with open("../pypoll/election_data.csv",'r',newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    vote_count = 0
    candidate_list = []
        

    for row in csvreader:
        vote_count += 1
        candidate_list.append(row[2])
    candidate_list = set(candidate_list)
    candidate_list = list(candidate_list)
        
    print("ELECTION RESULTS")
    print("---------------------------")
    print(f"Total Votes: {vote_count}")
    print("---------------------------")
    #print(candidate_list)

candidate_votes = [0,0,0,0]
with open("../pypoll/election_data.csv",'r',newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

    for row in csvreader:
        if row[2]== "Khan":
            candidate_votes[0]+=1        
        elif row[2]=="Li":
            candidate_votes[1]+=1
        elif row[2]== "O'Tooley":
            candidate_votes[2]+=1
        elif row[2]=="Correy":
            candidate_votes[3]+=1
    winner_index = candidate_votes.index(max(candidate_votes))
    winner = candidate_list[winner_index]

    p_khan = '%.2f'%((candidate_votes[0]/sum(candidate_votes))*100)
    p_li = '%.2f'%((candidate_votes[1]/sum(candidate_votes))*100)
    p_tooley = '%.2f'%((candidate_votes[2]/sum(candidate_votes))*100)
    p_correy = '%.2f'%((candidate_votes[3]/sum(candidate_votes))*100)

    print(f"{candidate_list[0]}: {p_khan}% ({candidate_votes[0]})")
    print(f"{candidate_list[1]}: {p_li}% ({candidate_votes[1]})")
    print(f"{candidate_list[2]}: {p_tooley}% ({candidate_votes[2]})")
    print(f"{candidate_list[3]}: {p_correy}% ({candidate_votes[3]})")
    print("---------------------------")
    print(f"The winner is: {winner}")
    print("---------------------------")

# Exporting results to txt file
f = open("../pypoll/election_results.txt","w+")
f.write("Election Results")
f.write("--------------------------")
f.write(f"Total Votes: {vote_count}")
f.write("--------------------------")
f.write(f"{candidate_list[0]}: {p_khan}% ({candidate_votes[0]})")
f.write(f"{candidate_list[1]}: {p_li}% ({candidate_votes[1]})")
f.write(f"{candidate_list[2]}: {p_tooley}% ({candidate_votes[2]})")
f.write(f"{candidate_list[3]}: {p_correy}% ({candidate_votes[3]})")
f.write("---------------------------")
f.write(f"The winner is: {winner}")
f.write("---------------------------")
f.close()