# Guess My Number
#
# The computer picks a random number between 1 and 10
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money

import random
print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 10'!")
print("Try to guess it in as few attemps as possible.\n")

#set the initial values
the_number = random.randint(1, 10)
tries = 1

# ask number
def ask_number(question, low, high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

# guessing loop
def main():
    guess = int(ask_number("Take a guess: ", 1, 10))    
    while guess != the_number:
        if guess > the_number:
            print("Lower...")
        elif guess < the_number:
            print("Higher...")
        else:
            print("Your guess is outside the range")

        guess = int(ask_number("Take a guess: ", 1, 10))
        global tries
        tries += 1
    return guess, tries

#start the program
main()

    
print("You guessed it! The number was", the_number)
print("And it only took you", tries, "tries!\n")
input("\nPress the enter key to exit.")
