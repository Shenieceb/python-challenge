#PyPoll\Resources\election_data.csv
import csv
import os
# Files to load and output (Remember to change these)
#file_to_load = os.path.join("Resources", "election_data.csv")
#file_to_output = os.path.join("analysis", "analysis.txt")

file_to_load= "PyPoll\Resources\election_data.csv"
file_to_output="analysis.txt"

total_number_of_votes_cast = 0
candidate_list = []
candidate_dict = {}

with open(file_to_load, newline='') as csvfile:

    election_data = csv.reader(csvfile, )
    #print("tomato")
   # print (election_data)

    #Read the header row
    """the next function tells csv module to remove the header row for the purposes for for loop below"""
    header = next(election_data)
    for row in election_data:


        """Print row means columns and if look below you can see where it pulled each row from each column only"""
       # print(row[0])
        #print(row[1])
        candidate=row[2]
        #print(candidate)


        total_number_of_votes_cast=total_number_of_votes_cast+1
        if candidate not in candidate_list:
            candidate_list.append(candidate)
            candidate_vote = 1
            candidate_dict[candidate] = candidate_vote
            
        else:
            candidate_dict[candidate] +=1
       # print(candidate_list)
       # print(candidate_dict)

       # exit() 
print(total_number_of_votes_cast)
print(candidate_list)
print(candidate_dict)
print("first candidate dictionary not sorted: --- ", candidate_dict)
"the lambda function loops through the keys of the dict"
candidate_dict = sorted(candidate_dict.items(), key=lambda x:x[1])
print("second candidate dictionary sorted: ---" ,candidate_dict)
winning_candidate=candidate_dict[-1][0]
print("winning candidate:  --", winning_candidate)
winning_candidate_votes =candidate_dict[-1][1]




with open(file_to_output, "w") as analysis_txt:
    analysis_data = (
        f'ELECTION RESULTS:\n'
        f'*******************************************\n'
        f'total votes for all candidates: {total_number_of_votes_cast}\n'
        f'*******************************************\n'
        f'The winner of the election based on popular vote is:{winning_candidate} with {winning_candidate_votes} in vote count \n'
        f'*******************************************\n'
        f'The breakdown of votes for all candidates: \n'
    )
    analysis_txt.write(analysis_data)
    for candidate_votes in candidate_dict:
        # print("value: " , candidate_votes[1])
        candidate_name = candidate_votes[0]
        candidate_total_votes = candidate_votes[1]
        candidate_percentage = float(candidate_votes[1])/float(total_number_of_votes_cast) *100
        # print("percentage of votes: ", candidate_percentage)
        candidate_voting_totals = f"{candidate_name}: {candidate_percentage:.3f}% ({candidate_total_votes})\n"
        print(candidate_voting_totals, end="")
        analysis_txt.write(candidate_voting_totals)







