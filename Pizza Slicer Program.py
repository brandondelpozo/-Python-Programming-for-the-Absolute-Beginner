#Pizza Slicer Program
print("Slicing 'Cheat sheet'")
"""
0   1   2   3   4   5
+___+___+___+___+___+
| p | i | z | z | a |
+___+___+___+___+___+
-5  -4  -3  -2  -1   
"""
print("Enter the beginning and ending index for your slice of 'pizza'")
print("Press enter key at 'Begin' to exit\n")


word = "pizza"
start = None

while start != "":
    start = input("\nStart: ")
    
    if start:
        start = int(start)
        finish = int(input("Finish: "))
        
    result = (word[start: finish])
    print("word[", start, ":", finish, "] is", result)


input("\n\nPress enter key to exit")

