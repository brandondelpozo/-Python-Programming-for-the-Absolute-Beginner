# Handle It
# Demonstrates handling exceptions

# try/except
try:
    num = float(input("Enter a number: "))
except:
    print("Something went wrong!")

# specifying exception type
"""try:
    num = float(input("\nEnter a number: "))
except ValueError:
    print("That was not a number!")"""

input("Press enter key to exit.")

# handle multiple exception types
print()
for value in (None, "Hi"):
    try:
        print("Attempting to convert", value, "-->", end=" ")
        print(float(value))



















        
        
