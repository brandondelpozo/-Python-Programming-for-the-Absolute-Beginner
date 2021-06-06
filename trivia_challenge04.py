# Trivia Challenge
# Trivia game that reads a plain text file

import sys
import pickle, shelve

def open_file(file_name, mode):
    """open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)
    
    question = next_line(the_file)

    answers = []
    for i in range(4):
        answers.append(next_line(the_file))

    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    explanation = next_line(the_file)
    
    points = next_line(the_file)
    
    return category, question, answers, correct, explanation, points
    
def welcome(title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to Trivia Challenge!\n")
    name = input("what's your name?: ")
    print("\nWelcome", name,"!")
    print("\n\t\t", title, "\n")
    
    return name
    
def main():
    trivia_file = open_file("trivia4.txt", "r")
    title = next_line(trivia_file)
    #welcome(title)
    name = welcome(title)
    score = 0
    
    # get first block
    category, question, answers, correct, explanation, points = next_block(trivia_file)
    while category:
        # ask a question
        print(category)
        print(question)
        for i in range(4):
            print("t", i+1, "-", answers[i])
    
        # get answer
        answer = input("What's your answer?: ")
    
        # check answer
        if answer == correct:
            print("\nRight", end=" ")
            score = score + int(points)
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print("Score:", score, "\n\n")
        
        # get next block
        category, question, answers, correct, explanation, points = next_block(trivia_file)
    
    trivia_file.close()  
            
    print("That was the last question!")
    print("You're final score is", score)
    
    # saving scores inside .txt
    print("Pickling score")
    f = open("listOfScores4.txt", "wb")
    pickle.dump(score, f)
    pickle.dump(name, f)
    f.close()
    
    # unpickling score
    print("\nUnpickling score.")
    f = open("listOfScores4.txt", "rb")
    score = pickle.load(f)
    name = pickle.load(f)
    #print(score)
    #print(name)
    print("Well done", name, "you got:", score)
    f.close()
    
    #print name to test if variable is inside this function
    #print(name)
    
main()
input("\n\nPress the enter key to exit")
