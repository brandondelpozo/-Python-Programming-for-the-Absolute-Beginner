# Who's your father program
# The program lets the user enter the name of a male
# and produce the name of his father

# pseudocode
"""
welcome user
set dictionary of males and fathers
ask user what father's name of a make does the user wants to know
print only father names
set input
"""
# Code Starts Here
print("""
    Welcome to Who's your Daddy Program made by Brandon Del Pozo
Write a male name to know his father's name.
""")
print("""
Choose an option:
    0. Exit
    1. Show current dictionary
    2. Edit a male son name
    3. Edit a father name
    4. Delete son-father pairs
    5. Add new son-father pair
    6. Look up grandfather
""")
dictionary = {"brandon":"jorge", "juan":"quique", "piero":"javier", "caleb":"juan", "javier":"papajuan"}
choice = None
while choice != "0":
    choice = input("\nChoose an option: ")
    if choice == "1":
        print(dictionary)
    elif choice == "2":
        male = input("Enter the male name you want to edit: ")
        if male in dictionary:
            new_name = input("Enter new name: ")
            dictionary[new_name] = dictionary[male]
            del dictionary[male]
    elif choice == "3":
        male = input("Enter the male name who father's name you want to edit: ")
        if male in dictionary:
            father = input("Enter his new father name: ")
            dictionary[male] = father
    elif choice == "4":
        male = input("Enter the male name and the son-father pair will be deleted: ")
        if male in dictionary:
            del dictionary[male]
        else:
            print("male name doesn't exist in dictionary")
    elif choice == "5":
        male = input("Enter a male name for the son: ")
        if male not in dictionary:
            father = input("Enter a father name for the son: ")
            dictionary[male] = father
    # look up grand father from grandson's name
    elif choice == "6":
        grandson = input("Write the grandson's name to know his grandfather name: ")
        if grandson in dictionary:
            father = dictionary[grandson]
            grandfather = dictionary[father]
            print(grandson, "grandfather's name is", grandfather)
    else:
        print("Please try adding a valid name")

print("Thank you see you later user")
input("\nPress enter key to exit")
