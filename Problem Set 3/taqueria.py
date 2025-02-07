def main():
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
    total = 0
    while True:
        #get an Item from the keyboard
        item = getInput()
        #Return True if item is on list or if it is ""
        if validateItem(item, menu):
            #Return true if the input was blank
            if isBlank(item):
                break
            else:
                total += menu[item]
                print("Total: $" + str(total))
        else:
            print("Please input a item on the menu")
    
    print("Total: $" + str(total))


def getInput():
    i = input("Item: ")
    return i.title()
    

#If item is on the menu OR if the item is "" then return true Else return false
def validateItem(i, m):
    valid = 0
    if i == "":
        return True
    try:
        valid = m[i]
    except KeyError:
        return False
    return True


def isBlank(i):
    if i == "":
        return True
    else:
        return False


main()