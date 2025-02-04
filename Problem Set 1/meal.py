#Will take in a time in millitary standard form then print out if it is time for a meal
def main():
    time = input("What time is it? ")
    #split the str into mins and hours 
    hour, min = time.split(":")
    ctime = convert(hour, min)
    #Check if the converted time is during a meal time
    if 7.0 <= ctime <= 8.0:
        print("breakfast time!")
    elif 12.0 <= ctime <= 13.0:
        print("lunch time!")
    elif 18.0 <= ctime <= 19.0:
        print("dinner time!")
    else:
        print("not a meal time")

#Convert the str of standard millitary time to a float
def convert(h, m):
    h = float(h)
    m = float(m)/60
    return h + m

main()