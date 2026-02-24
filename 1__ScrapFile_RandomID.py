import random
import time
import os

def userid():

    while True:

        UserID = input("\n- Input 3 digits ID: ")
        IDlen = len(UserID)

        try:
            UserID = int(UserID)
            if IDlen == 3:
                break
            else:
                print("* Must be 3 Digits!")

        except:
            print("* Must be Digits!")

    return UserID







MainBol = True

while MainBol == True:
    _ = os.system("clear")

    print(": ID Gen/Search :")
    print("1 - Generate ID")
    print("2 - Create ID")
    print("3 - Search ID")
    print("4 - Exit")



    while True:
        Userinp = input("\n- Choice: ")

        if Userinp == "":
                input("* Input Error...")
                break
        

        Userinp = int(Userinp)

        if Userinp == 1:


            RanId = int(random.random() * 1000)

            with open(f"/Users/mattlyndonabuel/Desktop/CODES/PY_PLAYGROUND/#SF1_RandomID/{RanId}.txt", "w") as gen:
                gen.write(f"+ ID: {RanId}")

            input(f"+ Generated ID: {RanId}")
            break

        elif Userinp == 2:
            
            UserID = userid()

            with open(f"/Users/mattlyndonabuel/Desktop/CODES/PY_PLAYGROUND/#SF1_RandomID/{UserID}.txt", "w") as Cret:
                Cret.write(f"+ ID: {UserID}")

            input(f"+ Created ID: {UserID}")
            break


        elif Userinp == 3:

            while True:
                RanId = input("\n- ID: ")
                if RanId != "":
                    try:
                        RanId == int(RanId)
                        break
                    except:
                        print("* Input Error!")

                else:
                    print("* Input Error!")
            
            check = (f"/Users/mattlyndonabuel/Desktop/CODES/PY_PLAYGROUND/#SF1_RandomID/{RanId}.txt")
            
            try:
                with open(check, 'r') as file:
                    content = file.read()
                    input("+ Found!")
                    break
                
            except:
                input("+ Not Found!")
                break
                
            # Handle the error gracefully, e.g., set default content
            content = ""
            



        elif Userinp == 4:
            print("+ Exiting Program", end="")
            for count in range(3):
                print(".", end="")
                time.sleep(0.6)
            print("\n")
            MainBol = False
            break

        
            
        else:
            input("* Input Error...")



