# program to shelve a list of people from a .txt
import pickle, shelve


print("Pickling lists.")
scores = [1, 3]
f = open("listOfScores.txt", "wb")
pickle.dump(scores, f)
f.close()

print("\nUnpickling lists.")
f = open("listOfScores.txt", "rb")
scores = pickle.load(f)
print(scores)
f.close()

print("\nShelving lists.")
s = shelve.open("listOfScores2.dat")
s["scores"] = [1, 3]
s.sync()

print("\nRetrieving lists from a shelved file:")
print("Scores -", s["scores"])
s.close()

input("\n\nPress the enter key to exit")
