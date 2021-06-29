#
# cointoss.py - simulate tossing a coin, read numtrials from command line
#
import sys
import random

if len(sys.argv) == 1:
    numtrials = 100
else:
    numtrials = int(sys.argv[1])

coin = ["head","tail"]
heads = 0
tails = 0

for i in range(numtrials):
    toss = random.choice(coin)
    if toss == "head":
        heads += 1
    else:
        tails += 1

print("\nThere were ", heads, "heads and ", tails, 
        "tails from", numtrials, "trials\n")
#print(str(heads) + "," + str(tails) + "," + str(numtrials))
