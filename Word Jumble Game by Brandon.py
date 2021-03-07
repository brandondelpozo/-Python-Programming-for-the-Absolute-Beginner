# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word
#-------pseudocode-------
"""
greeting to  player
Print indications to start playing
set a list of word to guess
Computer choose a word from the list
Computer jumble the word selected
computer ask player what's is his work guessed?

while word solected from tuple is different than word guessed by player
    Computer print You are wrong try again
    ask to enter the word again

print You guessed, the word chosen by computer is xyz
"""
#--Code Start Here--
print("\tWecome to Word Jumble!")
print("Unscreable the letters to make a word.")
print("Press the enter key at the prompt to quit\n")

import random
TUPLE = ("fly", "car", "bathroom", "water", "compensation")
wordTuple = random.choice(TUPLE)
wordShuffled = list(wordTuple)
random.shuffle(wordShuffled)
wordShuffled = ''.join(wordShuffled)
print("The jumble is: ", wordShuffled)

guess = None

while guess != "" and guess != wordTuple:
    guess = input("\nYour guess: ")
    if guess != wordTuple:
        print("That's not the word try again")

print("That's it! You guessed it!\n")
print("Thanks for playing.")
input("\n\nPress the enter key to exit.")
