num = [1, 2, 3, 6, 4, 5, 7, 5, 4, 4, 4, 0, 3, 0, 40, 8, 65, 42, 5, 1, 70, 0, 84, 84]
org = []
i = 0

count = len(num)


for items in range(count):
    take = max(num)
    num.remove(take)
    org.append(take)


print(f"\nList:", end=" ")

for items in org:
    print(org[i], end = "")
    i+=1
    if i > 0 and i != count:
        print(", ", end="")

print("\n")


chest = int()
hand = int()

i = 0

for items in org:
    if hand != chest:
       chesti = handi
    handi+=1



print("Secod Highest:", hand) 

print("")













































































