# High Scores 2.0
# Demonstrtes nested sequences

scores = []

choice = None
while choice != "0":
    print(
    """
    High Scores 2.0

    0 - Quit
    1 - Lists Scores
    2 - Add a Score
    """
    )
    choice = input("Choice: ")
    print()
    # exit
    if choice == "0":
        print("Good-bye.")
    # display high-scores table
    elif choice == "1":
        print("High Scores\n")
        print("NAME\tSCORE")
        for entry in scores:
            score, name = entry
            print(name, "\t", score)
    # add a score
    elif choice == "2":
        name = input("What is the player's name?: ")
        score = int(input("what score did the player get: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5] # keep only 5 top scores
    # some unknown choice
    else:
        print("sorry, but", choice, "isn't a valid choice.")

input("\n\nPress the enter key to exit.")



    
    
