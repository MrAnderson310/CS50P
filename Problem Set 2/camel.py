#Take in user input in camel case then refactor it to be in snake case
def main():
    x = input("camelCase: ")
    convertCase(x)
    
#Convert from camelCase to snake_case
def convertCase(case):
    #For each char in the input
    for i in case:
            #Check if the char is upper case
            if i.isupper():
                 #Change the char to lower case and print "_"
                 i = i.lower()
                 print("_", end="")
            #Print char
            print(i, end="")
    #print ending line break
    print()

main()