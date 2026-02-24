
import os

list = ["matt", "blue", "blue", "colleen", "yellow"]

buffer = str()
collect = str()

selected_color = "blue"

itemcount = 0

i = 0

for items in list:
    buffer = list[i]
    i += 1

    if buffer == selected_color:

        if itemcount > 0:
            collect += ", "

        collect += buffer
        itemcount += 1
    
_ = os.system("clear")

print("\n\n-------------------- Items --------------------\n")
print(f"Found Items({selected_color}): {collect}")
print(f"Total Items Found: {itemcount}\n\n")


