org = []
userorg = []



time = int(input("Times: "))

i = 1
for item in range(time):
    userin = int(input(f"Num{i}:"))
    org.append(userin)
    i+=1

count = len(org)

for items in range(count):
    take = max(org)
    org.remove(take)
    userorg.append(take)



print(f"\nList: {userorg}\n")
print("Second Highest:", userorg[1])


