def main():
    groceryList = {}
    while True:
        item = getItem()
        if item == "":
            break
        else:
            groceryList = appendItem(item, groceryList)
    
    sortedGroceryList = dict(sorted(groceryList.items()))
    for key, value in sortedGroceryList.items():
        print(f"{value}: {key}")
        

            

def appendItem(item, groceryList):
    if item in groceryList:
        groceryList[item] += 1
    else:
        groceryList[item] = 1
    return groceryList
    




def getItem():
    try:
        item = input("Item: ")
    except EOFError:
        return ""
    return item.capitalize()


main()