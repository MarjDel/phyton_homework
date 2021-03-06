#HOMEWORK2: Python_PyBank
title = "Financial Analysis"
print(title)

#1.The total number of months included in the dataset.
#HOMEWORK2: Python

#1.The total number of months included in the dataset.
#Declare variables
start_year = 2010
end_year = 2017
start_month = 0
end_month = 2

#Calculate total number of months
num_months =(end_year -start_year)* 12 + (end_month - start_month)
total_months = f"Total Months: {num_months}"

#Print the total number of months
print(total_months)

#2.The net total amount of Profit/Losses over the entire period.
#Import budget_data csv
import csv
with open("../homework_final/budget_data.csv",'r') as budget_data:
    rows=csv.reader(budget_data,delimiter=',')
    
    for r in rows:
        print (r[1])
     
        total_profit  = 0
        for r in rows:
            total_profit += (int(r[1]))    
    total_profit = f"Total Profit: $ {total_profit}"
    
#print the total profit output
    print(total_profit)


#3.The average of the changes in Profit/Losses over the entire period.
# Assign Variables
initial_profit = 867884
final_profit = 671099
num_months = 86

#Calculate the average profit
average_profit = {(final_profit - initial_profit)/((num_months)-1)}           
average_profit = f"Average Profit: $ {average_profit}"

#print the average profit output
print(average_profit)

#The greatest increase in profits (date and amount) over the entire period
  #initialize value  
    greatest_profit = r[0]
    
    for r in rows:
        greatest_profit.append(r[1])
    greatest_profit = max(greatest_profit, key=int)
    message = f"Greatest Increase in Profit:  $ {greatest_profit}"
    
    #print the greatest decrease in losses output
    print(message)
    

#The greatest decrease in losses (date and amount) over the entire period.
    #initialize value  
    decrease_losses = r[]
    
    for r in rows:
        decrease_losses.append(r[1])
    decrease_losses = max(decrease_losses, key=int)
    message = f"Greatest Decrease in Losses:  $ {decrease_losses}"
    
    #print the greatest decrease in losses output
    print(message)