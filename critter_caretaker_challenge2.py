# Television Caretaker
# A virtual pet to care for

class Television(object):
    """A virtual television"""
    def __init__(self, name, channelNumber = 0, volumeLevel = 0):
        self.name = name
        self.channelNumber = channelNumber
        self.volumeLevel = volumeLevel

    def __pass_time(self):
        self.channelNumber += 1
        self.volumeLevel += 1

    def talk(self):
        print("I'm", self.name, "and I'm at", self.channelNumber, "channel now.\n")

    def change(self, defaultChannel = 4):                    # If no value is passed, defaultChannel gets the default value of 4.
        defaultChannel = int(input("Choose a channel you want to watch in your Television from 1 to 4: "))
        print("You change the channel. Well done.")
        self.channelNumber = defaultChannel

    def volume(self, defaultVolume = 4):
        defaultVolume = int(input("How many volume do you want in your Television from 1 to 4? "))
        print("You change the volume. Awesome!")
        self.volumeLevel = defaultVolume

def main():
    television_name = input("What do you want to name your Television?: ")
    televi = Television(television_name)

    choice = None
    while choice != "0":
        print(
        """
        Television Caretaker

        0 - Quit
        1 - Current Channel in your Television
        2 - Enter a Channel for your Television
        3 - Choose a volume for your Television
        """)
        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # Enter a Channel for your Television
        elif choice == "1":
            televi.talk()

        # feed your Television
        elif choice == "2":
            televi.change()

        # Enter a volume in your Television
        elif choice == "3":
            televi.volume()

        # some unkown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
input("\n\nPress the enter key to exit.")











