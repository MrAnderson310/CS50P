def main():
    #Initialized list of months
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    #prompt the user to enter a date
    while True:
        date = getInput()
        #if the month is in the list then set the date = the number associated with that month
        if months.__contains__(date[0]):
            date[0] = months.index(date[0]) + 1
            break
        #Check if the month is in the allowed range
        elif 0 < int(date[0]) < 13:
            break
    
    printDate(date)



#Get an input from user in the MM/DD/YYYY format
def getInput():
    date = input("Date: ")
    if date.__contains__("/"):
        return date.split(sep="/")
    elif date.__contains__(","):
        return date.split(sep=",")
    
#Print the date inputed in the correct format
def printDate(d):
    print(d[2], end="-")
    print(d[0], end="-")
    print(d[1])


main()