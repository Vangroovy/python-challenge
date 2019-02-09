
## Financial Analysis Routine##

import csv
import os

def print_and_write(file, data):
    print(data, end="")
    file.write(data)

financials_csv=os.path.join("python-challenge", "pybank","budget_data_copy.csv")

##Open and read the CSV
with open(financials_csv, newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    ##Read the header row
    csvheader = next(csvfile)
    
    #Define variables

    dates = []
    no_months = 0
    total_profit_loss = 0
    profit_change = []
    last_profit_change = 0
        
    #Define and execute the calculations
    for row in csvreader: 
        #Create a list with the dates and changes
        dates.append(row[0])
            
        #count the number of months
        no_months = no_months + 1

        #Total profits/losses for the period    
        total_profit_loss = int(row[1]) + total_profit_loss

        #Calculate the change in profit month over month
        #Create a list of all the changes and save it
        profit_change.append(int(row[1]) - last_profit_change)
        last_profit_change = int(row[1])
     
    #Average of Changes in profit/loss over the period
    #Find the first variable in the list so it can be removed from the average calc
    first_profit_change = int(profit_change[0])   
    avg_change = (int(sum(profit_change)) - first_profit_change) / (no_months - 1)

    #What is the index of the greatest increase in profits over a period
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

    #Create the path for the filename
    financial_output=os.path.join("python-challenge", "pybank", "data.txt")

    #print and write the results
    with open(financial_output, "w", newline="") as textfile:
        print_and_write(textfile, "Financial Analysis \n")
        print_and_write(textfile, "------------------\n")
        print_and_write(textfile, "Total Months: %s \n" % no_months)
        print_and_write(textfile, "Total: $ %s \n" % total_profit_loss)
        print_and_write(textfile, "Average Change: $ %.2f \n" % avg_change)
        print_and_write(textfile, "Greatest Increase in Profits: %s ($%s)\n " % (max_change_date, max_change_amount))
        print_and_write(textfile, "Greatest Decrease in Profits: %s ($%s)\n" % (max_decrease_date, max_decrease_amount))     