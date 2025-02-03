#Prompt the user for a greeting if the greeting is Hello then print $0 if it starts with an h but is not Hello print $20 if it is anything else print $100
def main():
    g = input("Greeting: ")
    g = g.lower()
    #Checks if g is equal to hello
    if g == "hello":
        print("$0")
    #Checks if g starts with an "h"
    elif g.startswith("h"):
        print("$20")
    #Prints $100 if nothing else returned true
    else:
        print("$100")

main()