#Take in user input and remove all of the vowels
def main():
    x = input("Input: ")
    #For every char in the string check if the char is a vowel
    for c in x:
        if c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
            print("", end="")
        elif c == "A" or c == "E" or c == "I" or c == "O" or c == "U":
            print("", end="")
        else:
            print(c, end="")
    print()
main()