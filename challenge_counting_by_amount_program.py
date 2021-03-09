# Counting Program
# This program counts for the user, from
# beginning to end
#---pseudocode---

"""
#--Pseudocode--
computer ask for a start number
computer ask for a end number
computer ask for amount to count

while start plus count multiplied by n =< count
    start added the amount n times until start will be =< than end
the computer prints each number
"""
print("\tWelcome to Counting Program by amount")
print("\nThis program will count by amount from start to end\n\n")

start = int(input("Plese enter start number: "))
end = int(input("Plese end start number: "))
amount = int(input("Please enter the amout: "))

while start < end:
    start = start + amount
    if start < end:
        print(start)
    else:
        print("That's all my friend, thank you very much!")
    
input("\n\nPress enter key to exit")
