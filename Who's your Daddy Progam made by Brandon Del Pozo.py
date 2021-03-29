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
    Welcome to Who's your Daddy Program
Write a male name to know his father's name.
""")
print("""
Choose an option:
    0. Exit
    1. Show current dictionary
    2. Edit a male name
    3. Edit a father name
    4. Delete son-father pairs
""")
dictionary = {"jhon":"robert", "luis":"george", "juan":"pedro"}
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
    else:
        print("Please try adding a valid name")

print("Thank you see you later user")
input("\nPress enter key to exit")
