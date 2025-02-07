#Takes in User Input of their desired vanity plate
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 > len(s) > 6:
        return False
    #Check if c is a number then split the string into 2 substrings one for numbers and one for letters
    for i, c in enumerate(s):
        if c.isnumeric():
            foundNum = True
            numbers = s[i:]
            letters = s[:i]
        elif c.isalpha():
            pass
        else:
            return False

    #Check if letters are puctuation marks or spaces
    for char in letters:
        if char == " " or char == "." or char == "!" or char == "?":
            return False
        
    #Check if the first number is a 0 or if it is a "."because isnumeric doesn't check
    numcount = 0
    for n in numbers:
        if n == ".":
            return False
        elif n == "0" and numcount == 0:
            return False
        else:
            numcount += 1
    #Return True if all others pass
    return True
        
        
main()