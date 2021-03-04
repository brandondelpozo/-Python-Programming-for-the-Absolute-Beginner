#'Guess my Number 2 - Inversed' made by Brandon Del Pozo
# Player should choose a number from 1 to 10
# Computer should guess it

#Pseudocode
"""
Player insert a playerNumber from 1 to 10
The program set a programNumber
The program choose a random value and call it programNumber
player insert a value and call it playerNumber

while the programNumber is different than playerNumber execute
The Program ask if the playerNumber is higher or lower than programNumber
Player answer the question with 'H' or 'L'
    If it is higher the player say 'H' then
    the program set a random value to programNumber in between programNumber and 10
    and then try to guess again
    If it is higher the player say 'L' then
    the program set a random value to programNumber in between 0 and programNumber
    and then try to guess again

The program say You guess it
"""
#----Code Start Here-----
print("\t\tWelcome to Guess my Number reloaded")
print("Now you have to choose a aleatory number and the computer will try to guess it")
import random
programNumber = random.randint(1,10)
playerNumber = int(input("\nHello guesser please choose a number between 0 and 10: "))
answer = ""
programNumberMax = 10
programNumberMin = 1

while programNumber != playerNumber:
    answer = input("Is your number higher(h) or lower(l) than {} ?: ".format(programNumber))
    if answer == "h":
        programNumberMin = programNumber
        programNumber = random.randint(programNumberMin, programNumberMax)
    elif answer == "l":
        programNumberMax = programNumber
        programNumber = random.randint(programNumberMin, programNumberMax)
    else:
        print("Sorry I do not understand please enter h or l")
        
print("\nI guess it your number is ", playerNumber,"!")
input("\n\nPress enter to exit")

