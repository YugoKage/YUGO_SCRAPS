
userorg = []


time = int(input("Times: "))

i = 1
for item in range(time):
    userin = int(input(f"Num{i}:"))
    userorg.append(userin)
    i+=1

userorg.sort(reverse=True)

print(f"\nList: {userorg}")



saved = userorg[0]

for item in userorg:
    buffer = item
    if buffer < saved:
        saved = buffer
        break

print("Second Highest:", saved)

print("")


