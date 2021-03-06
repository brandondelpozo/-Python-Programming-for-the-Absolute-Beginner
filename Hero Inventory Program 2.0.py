# Hero's Inventory 2.0
# Demonstrates tuples

#crate a tuple with some items and display with a for loop
inventory=("sword",
       "armor",
       "shield",
       "healing potion")
print("Your items: ")
for item in inventory:
    print(item)

input("\nPress the enter key to continue.")
print("You have", len(inventory), "in you possession.")

#get the length of a tuple
input("\nPress the enter key to continue.")
if "healing potion" in inventory:
    print("You will live to fight another day.\n")

# display one item through an idex
index = int(input("Enter the index number for an item in inventory: "))
print("At index", index, "is", inventory[index])

# slice the tuple
start = int(input("\nEnter the index number to begin a slice: "))
end = int(input("Enter the end number to end the slice: "))
print("inventory[", start,":", end, "] is", inventory[start:end])

# concatenate two tuples
input("\nPress the enter key to continue.")
chest = ("gold", "gems")
print("You find a chest. It contains:")
print(chest)
print("You add the contents of the chest to your inventory.")
inventory += chest
print(inventory)

input("\nPress enter key to exit")

