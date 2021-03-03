"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

totals = {}

# Add up total call time per number
for line in calls:
    if line[0] in totals:
        totals[line[0]] += int(line[3])
    if line[1] in totals:
        totals[line[1]] += int(line[3])
    if line[0] not in totals and line[1] not in totals:
        totals[line[0]] = int(line[3])
        totals[line[1]] = int (line[3]) 


# Figure out greatest call time
biggestAmmount = 0
biggestNumber = 0

for x in totals:
    if totals[x] > biggestAmmount:
        biggestAmmount = totals[x]
        biggestNumber = x

print ("{} spent the longest time, {} seconds, on the phone during September 2016.".format(biggestNumber,biggestAmmount))
        



