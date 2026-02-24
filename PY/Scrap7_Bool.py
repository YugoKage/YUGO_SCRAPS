
name = str()
checkname = bool


while True:
    name = input("Please input name: ")

    if name != "":
        print(f"Name: {name}...")
        break
    else:
        print("Input Error...")
