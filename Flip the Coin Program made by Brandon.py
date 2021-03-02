# Flip the Coin Program
# The program count the number of head and tails of a coin flipped 100 times
"""
Set the coin value goes between head and tail randomly
Set number of flip = 1
flip the coin in the air
the coin show head or tail, 1st flip
the coin show head or tail, 2nd flip
the coin show head or tail, 3rd flip
.                              .
.                              .
.                              .
the coin show head or tail, 100th flip
count number of coin = head
count number of coint = tail
Show to user number of heads and tails

"""
print("\tWelcome to the Flip the Coin Program")
print("This program show the number of tales and heads, are you ready?")

import random
flip = 1
head = 0
tale = 0
while flip <= 10:
    valueCoin = random.randint(1,2)
    if valueCoin == 1:
        print("Head")
        head += 1        
    else:
        print("Tail")
        tale += 1
    flip += 1

print("\nThe number of tales is", tale)
print("The number of heads is", head)
input("\n\nPress enter to exit.")
