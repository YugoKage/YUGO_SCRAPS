

Box = 0

while Box < 5:
    Userint = int(input("Add to the Box an amount: "))
    Box = Userint + Box
    print("The Box now contains:", Box)

if Box <= 5:
    print("The Box is full!")

elif Box >= 5:
    print("Box is Over Flowing.")


