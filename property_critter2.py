# Property Critter
# Demonstrates properties

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, age):
        print("A new critter has been born!")
        self.__name = name   #this is a private attribute
        self.__age = age

    @property               #I use property here because I wanto to makes changes to the private attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("A critter's name can't be the empty string.")
        else:
            self.__name = new_name
            print("Name change successful.")

    def talk(self):
        print("\nHi, I'm", self.name, "I'm", self.age)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age == "":
            print("A critter's age can't be empty string")
        else:
            self.__age = new_age
            print("Age change successful.")

# main
crit = Critter("Jhony", 21)
crit.talk()

print("\nAttempting to change my critter's name to PocaPoca...")
crit.name = "PocaPoca"

print("My critter's name is:", end=" ")
print(crit.name)


print("\nAttempting to change my critter's age to 24...")
crit.age = 24

crit.talk()

"""
# main
crit = Critter("Poochie")
crit.talk()

print("\nMy critter's name is:", end=" ")
print(crit.name)

print("\nAttempting to change my critter's name to Randolph...")
crit.name = "Randolph"

print("My critter's name is:", end=" ")
print(crit.name)

print("\nAttempting to change my critter's name to the empty string...")
crit.name = ""

print("My critter's name is:", end=" ")
print(crit.name)
"""

input("\n\nPress enter key to exit")
