# Private Critter
# Demonstrates private variable and methods

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, mood):
        print("A new critter has been born!")
        self.name = name            # public attribute
        self.__mood = mood          # private attribute
        
    def talk(self):
        print("\nI'm", self.name)
        print("Right now I feel", self.__mood, "\n")

    def __private_method(self):     #two leading underscore to its name by convention
        print("This is a private method.")

    def public_method(self):
        print("This is a public method.")
        self.__private_method()

#crit = Critter(name = "Poochie", mood = "happy")
#print(crit._Critter__mood)       #private attribute hiden through a special naming convention '_'

#crit.private_method #'Critter' object has no attribute 'private_method'
#crit.__private_method() #'Critter' object has no attribute '__private_method'
#crit._Critter__private_method() #this is the way we can access a private method of a class

#main
crit = Critter(name="Poochie", mood= "happy")
crit.talk()
crit.public_method()

input("Press the enter key to exit")


