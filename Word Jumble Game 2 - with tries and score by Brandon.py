# Word Jumble 2 - with hints and score
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word
#-------pseudocode-------
"""
greeting to  player
Print indications to start playing
set a list of words to guess
set a tries to guess equal a number
Computer choose a word from the list
Computer jumble the word selected
computer ask player what's is his work guessed?

while word solected from tuple is different than word guessed by player
    Computer prints You are wrong try again
    tries icrement
    ask to enter the word again
    if tries is more than 3
    print("this is a hint")

print You guessed, the word chosen by computer is xyz

if tries less than 3
    print 'you got 50 point of 100'
else print you got 100

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
tries = 0

while guess != "" and guess != wordTuple:
    guess = input("\nYour guess: ")
    if guess != wordTuple:
        print("That's not the word try again")
        tries += 1
        if tries >= 3:
            print("I going to help you, this is a hint: ", wordTuple[:2])

print("That's it! You guessed it!\n")

if tries <3:
    print("You didn't use the hint, You got 100 point!")
else:
    print("As you use hint, you got only 50 points of 100")

print("Thanks for playing.")
input("\n\nPress the enter key to exit.")
