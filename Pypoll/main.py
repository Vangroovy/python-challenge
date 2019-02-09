#Election Result Analyzer

#Load file
import csv
import os

def print_and_write(file, data):
    print(data, end="")
    file.write(data)

election_csv=os.path.join("python-challenge", "PyPoll","election_data_copy.csv")

##Open and read the CSV
with open(election_csv, newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Read the header row
    csvheader= next(csvfile)
    
    #Define variables   
    candidate_vote_counts = {}    

    #Create dictionary to read all the votes, count the total and find unique candidates
    for row in csvreader: 
        candidate_name = row[2]
        if candidate_name in candidate_vote_counts:
            candidate_vote_counts[candidate_name] += 1
        else:
            candidate_vote_counts[candidate_name] = 1
    total_votes = sum(candidate_vote_counts.values())
   
    #Create the path for the filename
    output_file = os.path.join("python-challenge", "Pypoll", "data.txt")
    
    #Write data to a .txt file
    with open(output_file, "w", newline="") as textfile:
        print_and_write(textfile, "Election Results\n" )
        print_and_write(textfile, "--------------------------\n")
        print_and_write(textfile, "Total Votes: %s \n" % total_votes)
        print_and_write(textfile, "--------------------------\n")
        for candidate_name in candidate_vote_counts.keys():
            
            #Calculate the percentage of votes for each candidate
            percent_of_votes = candidate_vote_counts[candidate_name] / total_votes * 100  
            
            #Write the stats by candidate to the textfile
            print_and_write(textfile, "%s: %.3f %% (%i)\n" % (candidate_name, percent_of_votes, candidate_vote_counts[candidate_name]))
        
        #Winner equals the key with the largest value
        winner= max(candidate_vote_counts, key=candidate_vote_counts.get)
        
        #Write the winner information to the text file
        print_and_write(textfile, "-------------------------- \n")
        print_and_write(textfile, "The winner is: %s\n"% winner)
        print_and_write(textfile, "--------------------------\n")