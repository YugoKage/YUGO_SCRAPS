

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def multi(a, b):
    return a * b

def divide(a, b):
    return a / b



operators = ["+", "*", "/", "-"]

while True:
    dig1 = str(input("Digit 1: "))
    if dig1 != "":
        dig1 = int(dig1)
        break

while True:
    oper = input("Operator(+, -, *, /): ")
    passer = True

    if oper == "":
        print("Input Error...")
        passer == False
    else:
        if passer == True:
            if oper in operators:
                break
            else:
                print("Input Error...")


while True:
    dig2 = str(input("Digit 2: "))

    if dig2 != "":
        dig2 = int(dig2)
        break
  


match oper:
    case "+":
        result = plus(dig1, dig2)
    case "-":
        result = minus(dig1, dig2)
    case "/":
        result = divide(dig1, dig2)
    case "*":
        result = multi(dig1, dig2)


print(f"Result: {result:.2f}")
















