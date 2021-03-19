#Day9 Challenge 'Guess the letter Game'
#The program will ask you to guess a word
#from a list of words, and it gives us 5 attempts to guess the word by answering yes or no when the player sends a letter
#---Pseudocode---
"""
set a TUPLE with words
transform tuple into list
the program choose a word from list
wordChosen equal to the word from list
set guess equal none
while letter_guess different than string and letter_tries less than zero:
    letter_guess is an input that receive a letter
        if letter_guess in word:
            yes is inside
        else:
            try again
while guess different than string tries less than zero:
    if guess different than word:
        guess input enter a word
    if guess equal wordChosen
        print you are right
    else
        print try again
"""
#---Code starts here---
print(
"""            Welcome to Guess the letter program
You have limited chances to guess the word, good luck!
""")
import random
TUPLE = ("water", "cat", "mouse", "house")
list = list(TUPLE)
word = random.choice(list)
letters = len(word)
print("There are", letters, "letters in the word you have to guess.\n\n")
guess = None
tries = 1
letter_guess = None
letter_tries = 5
while letter_guess != "" and letter_tries>0:
    letter_guess = input("Enter a letter and I will tell you if is inside or no: ")
    letter_tries -= 1
    if letter_guess in word:
        print("You're right, that letter is inside the word\n")
    else:
        print("Sorry is not inside the word\n")
while guess != "" and tries>0:    
    guess = input("Enter your guess: ")
    tries -= 1
    if guess == word:
        print("You guess it\n")
    else:
        print("You didn't guess it")
        print("You have", tries, "tries left\n")
print("\nThat's all, thank you very much for playing this game")
input("Press enter to exit")
