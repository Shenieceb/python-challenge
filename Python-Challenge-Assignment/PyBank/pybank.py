import csv
import os
# Files to load and output (Remember to change these)
#file_to_load = os.path.join("Resources", "budget_data.csv")
#file_to_output = os.path.join("analysis", "analysis.txt")

file_to_load= r"C:\Users\glamh\OneDrive\Desktop\Python-Challenge-Assignment\PyBank\Resources\budget_data.csv"
#file_to_output="analysis.txt"




count_of_months=0
#starting_balance=0
total_profit_loss=0
with open(file_to_load, ) as csvfile:

    bank_data = csv.DictReader(csvfile)
    for row in bank_data:
        #print(row)
        #print(row['Date'], ' ', row['Profit/Losses'])
        #date=row['Date']
        #print(row['Profit/Losses'])
        count_of_months+=1
        starting_balance=int(row['Profit/Losses'])
       # print(starting_balance)
        total_profit_loss +=  starting_balance

        #print(total_profit_loss)
        #print (count_of_months)
print (count_of_months)
print(total_profit_loss)

 


