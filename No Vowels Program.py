# No Vowels Program
# Demonstrates creating new strings with a for loop

message = input("Enter a message: ")
new_message = ""
VOWELS = "aeiou"

for i in message:
    if i not in VOWELS:
        new_message += i
        print(i)
    

print("\nYour message without vowels is:", new_message)
input("\n\nPress enter key to exit")
