"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

count = 0
phone_numbers = []

for line in texts:
    if line[0] not in phone_numbers:
        phone_numbers.append(line[0])
    if line[1] not in phone_numbers:
        phone_numbers.append(line[1])

for line in calls:
    if line[0] not in phone_numbers:
        phone_numbers.append(line[0])
    if line[1] not in phone_numbers:
        phone_numbers.append(line[1])

print("There are {} different telephone numbers in the records.".format(len(phone_numbers)))

