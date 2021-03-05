# Random Acces Program
# Demonstrates string indexing

import random

word = input("Please enter a word: ")
print("The word is: ", word, "\n")

high = len(word)
low = -len(word)

for i in range(15):
    position = random.randrange(low, high)
    print("Word[", position, "]\t", word[position])


input("\n\nPress the enter key to exit")
