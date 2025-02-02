#Take in the meal amount and the desired tip amount and calculate how much to leave as a tip
#Take in user input then call dollars_to_float()
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = (dollars * percent)/100
    print(f"Leave ${tip:.2f}")

#take out the "$" in the input then cast the string as a float
def dollars_to_float(d):
    d = d.replace("$","")
    d = float(d)
    return d

#take out the "%" in the input then cast the string as a float
def percent_to_float(p):
    p = p.replace("%","")
    p = float(p)
    return p
#call main
main()