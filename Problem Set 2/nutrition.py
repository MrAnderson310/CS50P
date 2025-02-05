def main():
    #Dict of all of the fruits and their calorie count
    fruitDic = {
        "apple" : 130,
        "avacado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
    }

    #Get User Input and convert it to lowercase
    fruit = input("Item: ")
    fruit = fruit.lower()
    #Try to print the fruits cal count and exept a keyError if the input wasn't in the dict
    try:
        print(fruitDic[fruit])
    except KeyError:
        print("Not a Fruit on the list")

main()

        
