# Handle It
# Demonstrates handling exceptions

# try/except
"""
try:
    num = float(input("Enter a number: "))
except:
    print("Something went wrong!")

# Specifying exception type
try:
    num = float(input("\nEnter a number: "))
except ValueError:
    print("That was not a number!")


# Handle multiple exception types
print()
for value in (None, "Hi"):
    try:
        print("Attempting to convert", value, "-->", end=" ")
        print(float(value))

# Handle multiple exceptions types
print()
for value in (None, "Hi"):
    try:
        print("Attempting to convert", value, "-->", end=" ")
        print(float(value))
    except (TypeError, ValueError):
        print("Something went wrong!")

print()
for value in (None, "Hi"):
    try:
        print("Attempting to convert", value, "-->", end=" ")
        print(float(value))
    except TypeError:
        print("I can only convert a string or a number!")
    except ValueError:
        print("I can only convert a string of digits!")
"""
 
# get an exception's argument
try:
    num = float(input("\nEnter a number: "))
except ValueError as e:
    print("That was not a number! Or as Python would say...")
    print(e)

input("Press enter key to exit.")

        











        
        
