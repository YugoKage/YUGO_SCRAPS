
import os

_ = os.system('clear')

with open("TXT_FILES/Txt1.txt", "w") as file:
    
    file.write("Hello\n")
    
# Automatic na mo Close ang file, wala nay fclose()

