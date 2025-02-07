#Take in a fraction that looks like "X/Y" and changes into a int from 0 to 100%
def main():
    x = True
    #Keep trying to getLevel until the user enters a proper fraction
    while x == True:  
        amount = getLevel()
        #if getLevel returns false prompt them again
        if amount == False:
            "Please input a Proper Fraction"
        #else call doMath
        else:
            if doMath == -1:
                pass
            else:
                x = False
    print("Done")

    
            
            


def getLevel():
    while True:
        #Get input
        fuel = input("Fraction: ")
        #Split the input at a "/"
        fuelList = fuel.split(sep="/")
        #Try and see if the numerator is a number if it is not return false
        try:
            num = int(fuelList[0])
        except TypeError:
            return False
        #Try and see if the denominator is a number if it is not return false
        try:
            den = int(fuelList[1])
        except TypeError:
            return False
        #if numerator is bigger than denomator
        if num > den:
            return False
        else:
            #Return a list of the numbers [0] = num, [1] = den
            return fuelList
    
    
def doMath(list):
        x = 0
        #Try to divide the numbers and turn them into a percent if the denom is 0 prompt the user again
        try:
            percentage = (int(list[0])/int(list[1])) * 100
        except ZeroDivisionError:
            print("Please provide a denominator other than 0")
            x = -1
            return x
        #if the percentage is less than 1 print empty and if it is larger than 99 print full
        if percentage < 1:
            print("Empty")
        elif percentage > 99:
            print("Full")
        else:
            print(percentage + "%")
        return x



main()
