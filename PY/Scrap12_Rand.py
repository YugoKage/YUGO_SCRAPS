
import random



Range = str()
List = ["Single", "Married", "Dating"]

output = random.randint(1, 90)
output3 = random.choice(List)
output4 = bool(random.randint(0, 1))
output5 = int(random.random() * 10000000)

print("")

print("Age:", output)
print("Status:", output3)
print("Dead:", output4)
print("Random Seed:", output5)

print("")

