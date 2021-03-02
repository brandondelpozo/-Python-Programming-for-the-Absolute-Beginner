# Fortune Cookie Program
# pseudocode

'''The program display a 'fortune phrase'

give intrucctions

set the sentry variable from 1 to 5
select randomly one fortune phrase
    set the the first fortune phrase
    set the the second fortune phrase
    set the the third fortune phrase
    set the the fourth fortune phrase
    set the the fith fortune phrase
print the fortune frase choosen

input press enter to exit'''

#------------------------------

print("Welcome to the Fortune Cookie Program")
print("What's your fortune today?\n")

import random
fortuneNumber = random.randint(1,5)

if fortuneNumber == 1:
    print("'You will find the love of your life tomorrow.'")
elif fortuneNumber == 2:
    print("'Eyes don't heart doesn't feel.'")
elif fortuneNumber == 3:
    print("'Don't look a gift horse in the mouth.'")
elif fortuneNumber == 4:
    print("'A crisis is an opportunity riding the dangerous wind.'")
else:
    print("'A little impatience will spoil great plans.'")

input("\n\nPress enter to exit.")















