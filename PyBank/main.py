#PyBank
import os
import csv

def retrievebankinfo(csv):
    totalPnL = 0
    maxdifrev = 0
    mindifrev = 0
    months = 0
    avgchange = 0
    maxdifmonth = ""
    mindifmonth = ""
    lastmonth = None
    lastmonth_PnL = 0
    changes = []
    for row in csv:
        current_month = row[0]
        current_PnL = int(row[1])
        totalPnL += current_PnL
        months += 1
        if lastmonth is not None:
            current_change = current_PnL - lastmonth_PnL
            changes.append(current_change)
            if current_change > maxdifrev:
                maxdifrev = current_change
                maxdifmonth = current_month
            if current_change < mindifrev:
                mindifrev = current_change
                mindifmonth = current_month
        lastmonth = current_month
        lastmonth_PnL = current_PnL
    avgchange = sum(changes)/len(changes)
    return [months,totalPnL, maxdifrev, mindifrev, avgchange, maxdifmonth, mindifmonth]

with open ("budget_data.csv") as file:
    csvreader = csv.reader(file, delimiter = ",")   
    header = next(csvreader)
    analysis = retrievebankinfo(csvreader)

print(f"""
Financial Analysis
__________________________
Total Months: {analysis[0]}
Total: ${round(analysis[1], 2)}
Average Change: ${round(analysis[4], 2)}
Greatest Increase: {analysis[5]} (${analysis[2]})
Greatest Decrease: {analysis[6]} (${analysis[3]})
    """)


with open ("output.txt","w") as homework:
    homework.writelines(f"""
Financial Analysis
__________________________
Total Months: {analysis[0]}
Total: ${round(analysis[1], 2)}
Average Change: ${round(analysis[4], 2)}
Greatest Increase: {analysis[5]} (${analysis[2]})
Greatest Decrease: {analysis[6]} (${analysis[3]})
    """)