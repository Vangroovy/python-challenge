#Election Result Analyzer

#Load file
import csv
import os

##Import the file
election_csv=os.path.join("python-challenge", "PyPoll","election_data_copy.csv")

##Open and read the CSV
with open(election_csv, newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Read the header row
    csvheader= next(csvfile)
    
    #Define variables
    votes_list = []    
    candidate_list = []
    total_votes = 0 
    percent_of_votes = []
    candidate_total_votes = []
    final_stats_percentage=[]

    #Create Loop to read all the votes, count the total and find unique candidates
    for row in csvreader: 
        #Create a list with all the votes
        votes_list.append(row[2])
        
        #find unique candidates and build a list
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
    for cname in candidate_list:
        
        #Calculate the percentage of votes for each candidate
        percent_of_votes = votes_list.count(cname)/total_votes*100

        #Calculate the votes by candidate
        vote_by_candidate = votes_list.count(cname)

        #Print the stats by candidate
        #print(cname,":", round(percent_of_votes),"%", "(", vote_by_candidate, ')')
        print("%s: %.3f %% ( %i )" % (cname, percent_of_votes, vote_by_candidate))  

        #Save the vote_by_candidate into a list
        final_stats_percentage.append(percent_of_votes)
        candidate_total_votes.append(vote_by_candidate) 
    
    #Find the index with the most votes
    winner_index = final_stats_percentage.index(max(final_stats_percentage))
    
    #Use index to assign name of winner
    winner = str(candidate_list[winner_index])
    print("--------------------------")
    print("The winner is: ",winner)
    print("--------------------------")

    #Create the path for the filename
    output_file = os.path.join("python-challenge", "Pypoll", "data.txt")
    
    #Write data to a .txt file
    with open(output_file, "w", newline="") as textfile:
        textfile.write("Election Results\n" )
        textfile.write("--------------------------\n")
        textfile.write("Total Votes: %s \n" % total_votes)
        textfile.write("--------------------------\n")
        for cname in candidate_list:
            textfile.write("%s: " % cname)
            textfile.write("%.3f%% " % (votes_list.count(cname)/total_votes*100))
            textfile.write("(%d) \n" % votes_list.count(cname))
        textfile.write("-------------------------- \n")
        textfile.write("The winner is: %s\n"% winner)
        textfile.write("--------------------------")
    