
## Financial Analysis Routine##

import csv
import os

##Import the file
financials_csv=os.path.join("python-challenge", "pybank","budget_data_copy.csv")

##Open and read the CSV
with open(financials_csv, newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    ##Read the header row
    csvheader= next(csvfile)
    
    #Define variables
    no_months=0
    total_profit_loss = 0
    avg_change=0
    first_profit_change = 0
    last_profit_change=0
    profit_change = []
    dates = []
    
    #Define and execute the calculations
    for row in csvreader: 
        #Create a list with the dates and changes
        dates.append(row[0])
            
        #count the number of months
        no_months = no_months+1

        #Total profits/losses for the period    
        total_profit_loss = int(row[1])+ total_profit_loss

        #Calculate the change in profit month over month
        #Create a list of all the changes and save it
        profit_change.append(int(row[1])-last_profit_change)
        last_profit_change=int(row[1])
     
    #Average of Changes in profit/loss over the period
    #Find the first variable in the list so it can be removed from the average calc
    first_profit_change = int(profit_change[0])   
    avg_change = (int(sum(profit_change))- first_profit_change)/(no_months-1)

    #Determine the greatest increase in profits over a period
    #What is the index of the max value
    max_change_index = profit_change.index(max(profit_change))
    
    #Assign the value to the date and the amount of the decrease
    max_change_date= dates[max_change_index]
    max_change_amount = profit_change[max_change_index]
            
    #Determine the greatest decrease in losses(date and amount) over a period
    #find the index of the period with the greatest decrease in profits
    max_decrease_index = profit_change.index(min(profit_change))

    #Assign the value to the date and the amount of the decrease
    max_decrease_date = dates[max_decrease_index]
    max_decrease_amount = profit_change[max_decrease_index]
 
    #Print the results
    print("Financial Analysis")
    print("__________________")
    print(f"Total Months: ", no_months)
    print(f"Total: $", total_profit_loss)
    print(f"Average Change: $", avg_change)
    print(f"Greatest Increase in Profits: ", max_change_date, " $", 
            max_change_amount)
    print(f"Greatest Decrease in Profits: ", max_decrease_date, " $",
            max_decrease_amount)

    #Write the results to a text file
    import csv
    
    #Create results list
    output_data=[no_months, total_profit_loss,avg_change, max_change_date, 
    max_change_amount, max_decrease_date, max_decrease_amount]

    #Create the path for the filename
    financial_output=os.path.join("python-challenge", "Pybank", "data.csv")

    #write data to a .csv file
    with open(financial_output, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=",")
        writer.writerow(["Total months", "Total profit/loss", "Average change",
                        "Date of greatest increase in profits", "Increase in profits",
                         "Date of greatest decrease in profits", "Greatest decrease in profits"])
        writer.writerow(output_data)
       
        


        
        