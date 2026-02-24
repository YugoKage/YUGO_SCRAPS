
# IMPORTS

import os

import time






# FUNCTIONS ===================

def intro():

    print("\n\nYou found a Cave near Your village, You Smell Bread Inside...\n")

    print(input("Enter the Cave...(Enter): "))

    print(input("You light up your lantern and Enter..."))
    time.sleep(0.5)
    print("As you go deeper, the sweet odor of bread turns into...") 
    time.sleep(0.8)
    print("An unbearable stench of rotten meat, engulfing your surrounding.")
    time.sleep(0.8)
    print("But you see a dim of light ahead of you.\n")
    time.sleep(1)
    input("You go in deeper...")


    time.sleep(1)

    print("\n\nCrack!!!\n\n")

    time.sleep(0.5)


    print("-------------------------")
    time.sleep(0.02)
    print("                    -*-  ")
    time.sleep(0.02)
    print("--------x.     .x--------")
    time.sleep(0.02)
    print("         |     |         ")
    time.sleep(0.02)
    print("         |  V  |         ")
    time.sleep(0.02)
    print("         | -|- |         ")
    time.sleep(0.02)
    print("         |  o  |         ")
    time.sleep(0.02)
    print("         |     |         ")
    time.sleep(0.02)

    for deep in range(10):
        print("         |     |         ")
        time.sleep(0.05)

    for deep in range(10):
        print("         |.....|         ")
        time.sleep(0.05)

    for deep in range(10):
        print("         |*****|         ")
        time.sleep(0.05)

    for deep in range(10):
        print("         |00000|         ")
        time.sleep(0.05)

    for deep in range(50):
        print("         |@@@@@|         ")
        time.sleep(0.05)

    for deep in range(19):
        print("         |00000|         ")
        time.sleep(0.05)

    for deep in range(15):
        print("         |*****|         ")
        time.sleep(0.05)

    for deep in range(12):
        print("         |.....|         ")
        time.sleep(0.05)

    for deep in range(14):
        print("         |     |         ")
        time.sleep(0.05)

    for deep in range(13):
        print("         .     .         ")
        time.sleep(0.05)

    for deep in range(40):
        print("")
        time.sleep(0.05)

    _ = os.system("clear")







def ManuRdHelthPlayer(): #ROUND PLAYER HEALTH 2 Decimals
    global Player_Hp
    Player_Hp = round(Player_Hp, 2)

def ManuRdDmgPlayer(): #ROUND PLAYER DMG 2 Decimals
    global Player_Dmg
    Player_Dmg = round(Player_Dmg, 2)

# -------------------------------------------

def PlayerHurt(a): #PLAYER GETS DAMAGED WITH ROUND 2 Decimals
    global Player_Hp
    Player_Hp -= a
    ManuRdHelthPlayer()
    return Player_Hp

def DmgUpdPlayer(a): #PLAYER DAMAGE UPDATE WITH 2 Decimals
    global Player_Dmg
    Player_Dmg += a
    ManuRdDmgPlayer()
    return Player_Dmg
    











# VARIABLES ===================

Player_Hp = 100.00
Player_Dmg = float()
Player_Current = int(50)











# MAIN ========================

_ = os.system("clear") #### CLEAR START

intro()

print("\nDUNGEON...\n\n\n")





























