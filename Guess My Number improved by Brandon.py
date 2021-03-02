# Guess My Number Improved
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money

import random
print("\tWelcome to 'Guess My Number Improved'!")
print("\nI'm thinking of a number between 1 and 100'!")
print("Try to guess it in 3 attemps or loose the game.\n")

#set the initial values
the_number = random.randint(1, 10)
guess = int(input("Take a guess: "))
tries = 1
attemp = 2

# guessing loop
while guess != the_number and attemp >= 0:
    if guess > the_number:
        print("Lower...")
        print("You only have", attemp, "attemp left\n")
    else:
        print("Higher...")
        print("You only have", attemp, "attemp left\n")
    tries += 1
    
    if attemp > 0:
        guess = int(input("Take a guess: "))
        attemp -= 1
    elif attemp == 0:
        print("Sorry you didn't guess it, maybe next time :)")
        break

print("You guessed it! The number was", the_number)
print("Looks like you are a prossional guesser")
#print("And it only took you", tries, "tries!\n")
input("\n\nPress the enter key to exit.")
