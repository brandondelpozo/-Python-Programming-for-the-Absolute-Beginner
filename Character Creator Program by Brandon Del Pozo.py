# pseudocode
"""
set a dictionary with Strength, Health, Wisdom and Dexterity
sum of values less than 30
option 1 is to change key from dictionary
print dictionary
"""

# code
print("\tWelcome to the Character Creator Program made by Brandon Del Pozo.\n")
print("Take into account: Your total power can't sum more than 30 points.\n")
print(
    """
Choose an option:
    0. exit
    1. See my current value.
    2. Change value of character.
    3. See total of power
""")
abilities = {"strength":1, "health":2, "wisdom":3, "dexterity":4}
choice = None
total_power = 0

while choice != "0" and total_power <= 30:
    choice = input("Choose an option: ")
    hero_power = abilities.values()
    total_power = sum(hero_power)
    if choice == "1":
        print(abilities,"\n")
    elif choice == "2":
        ability = input("What ability do you want to change?: ")
        if ability in abilities:
            new_value = int(input("Enter new value: "))
            abilities[ability] = new_value
            print("New value has been changed\n")
        else:
            print("That ability does't exist! Try again\n")
    elif choice == "3":
        print(total_power,"\n")
    elif choice == "0":
        print("Thank you, bye")
    else:
        print("Please choose a valid option\n")
total_power
              
print("Thank you for playing this game\n")

input("\n\nEnter enter key to exit")
