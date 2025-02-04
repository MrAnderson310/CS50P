#take user input of a math expression and print the result, assume a space between all parts of expression given
def main():
    e = input("Expression: ")
    x, y, z = e.split()
    x = float(x)
    z = float(z)
    #Determine which operation to do
    match y:
        case "+":
            add(x, z)
        case "-":
            sub(x, z)
        case "*":
            mult(x, z)
        case "/":
            div(x, z)
        case _:
            print("please input a math operator")

#Prints the result of the operation
def add(a, b):
    print(a + b)

def sub(a, b):
    print(a - b)

def mult(a, b):
    print(a * b)

def div(a, b):
    print(a / b)

main()