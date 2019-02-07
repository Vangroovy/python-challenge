#Election Result Analyzer

#Load file
import csv
import os

##Import the file
election_csv=os.path.join("python-challenge", "PyPoll","election_data_copy.csv")

##Open and read the CSV
with open(election_csv, newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    ##Read the header row
    csvheader= next(csvfile)
    print("Header:", csvheader)
    
    #Define variables
    total_votes = 0    
    total_winning_votes = 0
    vote_by_candidate = []
    candidate_list = []
    vote = []
    percent_of_votes = 0
    no_candidates = 0
    total_votes_candidate = []

    #Create Loop
    for row in csvreader: 
        #Create a list with all the candidate votes
        total_votes_candidate.append(row[2])
        
        #find unique candidates
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
        
        #Calculate the total votes cast
        total_votes = total_votes+1   
    
    #Print results in table
    print("Election Results")
    print("--------------------------")
    print("Total Votes: ", total_votes)
    print("--------------------------")

    #Compute and print stats by candidate
    for candidate in candidate_list:
        #Create a string for the candidate name for comparison
        cname= str(candidate)
        
        #Calculate the percentage of votes for each candidate
        percent_of_votes= int(total_votes_candidate.count(cname))/total_votes*100

        #Calculdate the votes by candidate
        vote_by_candidate = total_votes_candidate.count(cname)

        #Print the stats by candidate
        print(cname,":", percent_of_votes,"%", "(", vote_by_candidate , ')')  
        
#Election winner based on popular vote

#Export text file with results
