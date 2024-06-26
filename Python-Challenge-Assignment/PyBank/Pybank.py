import csv
import os
# Files to load and output (Remember to change these)
#file_to_load = "Resources\budget_data.csv"
#file_to_output = "analysis\analysis.txt"

file_to_load= r"Python-Challenge-Assignment\PyBank\Resources\budget_data.csv"
file_to_output= r"Python-Challenge-Assignment\PyBank\analysis\budget_analysis.txt"

count_of_months=0
month_of_change=[]
netchange_list=[]
greatest_increase=["",0]
greatest_decrease=["",9999999999999999999]
total_profit_loss=0
with open(file_to_load) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    #print(header)
    first_row=next(csvreader)
    #print(first_row)
    count_of_months+=1
    total_profit_loss=int(first_row[1])

    prev_net=int(first_row[1])
    #print(prev_net)
    for row in csvreader:
        count_of_months+=1
        total_profit_loss+=int(row[1])
        net_change=int(row[1])-prev_net
        prev_net=int(row[1])
        netchange_list.append(net_change)
        month_of_change.append(row[0])
        if net_change>greatest_increase[1]:
            greatest_increase[0]=row[0]
            greatest_increase[1]=net_change
        if net_change<greatest_decrease[1]:
            greatest_decrease[0]=row[0]
            greatest_decrease[1]=net_change

average_change=sum(netchange_list)/len(netchange_list)
output=(
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {count_of_months}\n"
    f"Total: ${total_profit_loss}\n"
    f"Average  Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)
print(output)
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)