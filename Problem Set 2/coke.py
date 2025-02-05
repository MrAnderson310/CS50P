#A coke costs 50 units
#keep prompting the user until they have paid for a coke with 5, 10, and 25 unit increments
def main():
    owed = 50
    #Keep Prompting the user for coins
    while 0 == 0:
        x = int(input("Insert Coin: "))
        #when a coin is inserted call coinInsert
        owed = coinInsert(x, owed)
        if owed <= 0:
            break
        else:
            print("Amount Still Owed: ", end="")
            print(owed)
    checkForChange(owed)


def coinInsert(value, owed):
    #Check if the value the user inserted is an accepted value
    if value == 25:
        owed -= 25
    elif value == 10:
        owed -= 10
    elif value == 5:
        owed -= 5
    else:
        print("Please insert valid coin value")
    return owed

#Prints out the absolute value of the amount owed
def checkForChange(change):
    print("Change owed: ", end="")
    print(abs(change))

main()