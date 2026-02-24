

def Plus(a, b):
    return a + b

def Minus(a, b):
    return a - b

def Divide(a, b):
    return a / b

def Multi(a, b):
    return a * b





InputCor = 0
Total = int

print("\n\n---- Calculator ----\n")
Digit1 = int(input("Please Enter First Digit: "))

while True:
    Symbol = input("Please Choose (+, -, /, *): ")

    if Symbol == "+" or Symbol == "-" or Symbol == "/" or Symbol == "*":
        break
    else:
        print("input Error!")


Digit2 = int(input("Please Enter Second Digit: "))

match Symbol:
    case "+":
        Total = Plus(Digit1, Digit2)
    case "-":
        Total = Minus(Digit1, Digit2)
    case "/":
        Total = Divide(Digit1, Digit2)
    case "*":
        Total = Multi(Digit1, Digit2)

print(f"\nTotal: {Total} \n")








