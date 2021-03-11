# Print Backwards Program
#---pseudocode--
"""
welcome to user and print instructions
computer ask for a word

declare a None variable
while word different than string
    askfor a input word
    reverse the word with list comprehesion
    print the word

thank to he user
"""
print("\tWelcome to Print Backwards Program")
print("Please enter a word and see the magic happens!")
word = None

while word != "":
    word = input("\nEnter a word: ")
    reverse = word[::-1]
    print(reverse)
print("Thanks for playing this game")

input("\n\nPress the enter key to exit")
