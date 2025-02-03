#Ask the user the meaning of life if it is 42 then answer yes
def main():
    a = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    if isFortyTwo(a):
        print("Yes")
    else:
        print("No")

#Takes the users input and returns True if it is equal to 42
def isFortyTwo(s):
    #Turns the characters to lower case
    s = s.lower()
    #Using a match statment check if s is equal to any variation of 42
    match s: 
        case "42" | "forty two" | "forty-two":
            return True
        case _:
            return False
        
main()
