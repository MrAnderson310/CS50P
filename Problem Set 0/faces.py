#Takes input from user and replaces all ":)" with "🙂" and all ":(" with "🙁" then prints it back
#Replaces ":)" with "🙂" and ":(" with "🙁" then returns it 
def convert(x):
    x = x.replace(":)", "🙂")
    x = x.replace(":(", "🙁")
    return x
#Gets user input then calls covert(x) then prints the return of convert(x)
def main():
    x = input()
    y = convert(x)
    print(y)
#Calls main()
main()