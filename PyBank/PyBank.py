# PyBank Financial Analysis
#--------------------------------------------------
import csv

with open('budget_data.csv','r',newline ='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    i = next(csvreader)
    row_count = 0
    profits = []
    for row in csvreader:
        row_count += 1
        profits.append(row[1])

profits = list(map(int, profits))   

# Net Total amount of profit/losses 
net_profit = sum(profits)

# Average Changes
avg = '%.2f'%(net_profit/len(profits))
    
#Greatest Increase
max_increase = max(profits)
with open('budget_data.csv','r',newline ='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    i = next(csvreader)
    for row in csvreader:
        if int(row[1]) == (max_increase):
            max_date = row[0]

#Greatest Decrease
max_decrease = min(profits)
with open('budget_data.csv','r',newline ='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    i = next(csvreader)
    for row in csvreader:
        if int(row[1]) == max_decrease:
            min_date = row[0]

# Printing results
print("Financial Analysis\n-----------------------------")
print(f"Total months: {row_count} ")
print(f"Total: ${net_profit}")
print(f"Average Change: ${avg}")
print(f"Greatest Increase in Profits: {max_date} (${max_increase})")
print(f'Greatest Decrease in Profits: {min_date} (${max_decrease})')

# Exporting results to txt file
f = open("PyBank_Results.txt","w+")
f.write("Financial Analysis\n-----------------------------")
f.write(f"\nTotal months: {row_count}")
f.write(f"\nTotal: ${net_profit}")
f.write(f"\nAverage Change: ${avg}")
f.write(f"\nGreatest Increase in Profits: {max_date} (${max_increase})")
f.write(f"\nGreatest Decrease in Profits: {min_date} (${max_decrease})")
f.close()