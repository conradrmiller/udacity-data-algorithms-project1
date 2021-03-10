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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# Possible telemarketers:
# Make outgoing calls
# Never send texts
# Never recieve texts
# Never recieve incoming calls

sent_texts = []
recieved_texts = []
recieved_incoming_calls = []
possible_telemarketer = []

for line in calls:
    if line[1] not in recieved_incoming_calls:
        recieved_incoming_calls.append(line[1])

for line in texts:
    if line[0] not in sent_texts:
        sent_texts.append(line[0])
    if line[1] not in recieved_texts:
        recieved_texts.append(line[1])

for line in calls:
    if line[0] not in sent_texts:
        if line[0] not in recieved_texts:
            if line[0] not in recieved_incoming_calls:
                if line[0] not in possible_telemarketer:
                    possible_telemarketer.append(line[0])

possible_telemarketer.sort()
print ("These numbers could be telemarketers: ")
print(*possible_telemarketer, sep="\n")

# Big O Estimation:
# This algorithm is most likely runs in some version of linear time, something like O(3n).

