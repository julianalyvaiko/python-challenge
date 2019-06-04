import os
import csv

csv_path = os.path.join('budget_data.csv')


#set the output of the text file
text_path = "output.txt"

#Set variables
total_months = 0
total_revenue= 0
revenue = []
previous_revenue = 0
month_of_change = []
revenue_change = 0
greatest_decrease_in_Profit= ["", 9999999]
greatest_increase_in_Profit = ["", 0]
revenue_change_list = []
revenue_average = 0


#open the csv file
with open('budget_data.csv',newline='') as csvfile:  
    csvreader = csv.reader(csvfile, delimiter =',')
    csvheader = next(csvreader)

    #Loop through to find total months
    for row in csvreader:

        #Count the total of months
        total_months += 1

        #Calculate the total over the entire period
        print(row[1])
        total_revenue = total_revenue + int(row[1])

        #Calculate the average change in revenue between months over the entire period
        revenue_change = float(row[1])- previous_revenue
        previous_revenue = float(row[1])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = [month_of_change] + [row[0]]
       

        #The greatest increase in revenue (date and amount) over the entire period
        if revenue_change>greatest_increase_in_Profit[1]:
            greatest_increase_in_Profit[1]= revenue_change
            greatest_increase_in_Profit[0] = row[0]

        #The greatest decrease in revenue (date and amount) over the entire period
        if revenue_change<greatest_decrease_in_Profit[1]:
            greatest_decrease_in_Profit[1]= revenue_change
            greatest_decrease_in_Profit[0] = row[0]
    revenue_average = sum(revenue_change_list)/len(revenue_change_list)

#write changes to csv
with open(text_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write("Total Months: %d\n" % total_months)
    file.write("Total Revenue: $%d\n" % total_revenue)
    file.write("Average Revenue Change $%d\n" % revenue_average)
    file.write("Greatest Increase in Revenue: %s ($%s)\n" % (greatest_increase_in_Profit[0], greatest_increase_in_Profit[1]))
    file.write("Greatest Decrease in Revenue: %s ($%s)\n" % (greatest_decrease_in_Profit[0], greatest_decrease_in_Profit[1]))
