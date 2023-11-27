import csv
import os
# Files to load and output (Remember to change these)
#file_to_load = os.path.join("Resources", "budget_data.csv")
#file_to_output = os.path.join("analysis", "analysis.txt")

file_to_load= r"C:\Users\glamh\OneDrive\Desktop\Python-Challenge-Assignment\PyBank\Resources\budget_data.csv"
#file_to_output="analysis.txt"




count_of_months=0
with open(file_to_load, ) as csvfile:

    bank_data = csv.DictReader(csvfile)
    for row in bank_data:
        #print(row)
        count_of_months+=1



        #print (count_of_months)
print (count_of_months)


