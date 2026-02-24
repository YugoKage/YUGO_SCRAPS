
import os
import random


Cards = [
    "Ace of Spades", "2 of Spades", "3 of Spades", "4 of Spades", "5 of Spades",
    "6 of Spades", "7 of Spades", "8 of Spades", "9 of Spades", "10 of Spades",
    "Jack of Spades", "Queen of Spades", "King of Spades",

    "Ace of Hearts", "2 of Hearts", "3 of Hearts", "4 of Hearts", "5 of Hearts",
    "6 of Hearts", "7 of Hearts", "8 of Hearts", "9 of Hearts", "10 of Hearts",
    "Jack of Hearts", "Queen of Hearts", "King of Hearts",

    "Ace of Diamonds", "2 of Diamonds", "3 of Diamonds", "4 of Diamonds", "5 of Diamonds",
    "6 of Diamonds", "7 of Diamonds", "8 of Diamonds", "9 of Diamonds", "10 of Diamonds",
    "Jack of Diamonds", "Queen of Diamonds", "King of Diamonds",

    "Ace of Clubs", "2 of Clubs", "3 of Clubs", "4 of Clubs", "5 of Clubs",
    "6 of Clubs", "7 of Clubs", "8 of Clubs", "9 of Clubs", "10 of Clubs",
    "Jack of Clubs", "Queen of Clubs", "King of Clubs"
    ]

print("\n\nWelcome to the Card Drawer!\n")

UserInput = input("Draw 3 cards? (y/n): ")

while True:

    if UserInput == "n":
        print("\n- Exiting...\n\n")
        exit()

    elif UserInput.lower() == "y":

        _ = os.system('clear')

        Set1 = random.choice(Cards)
        Set2 = random.choice(Cards)
        Set3 = random.choice(Cards)
        print("\nYour drawn cards are:")
        print("1.", Set1)
        print("2.", Set2)
        print("3.", Set3)
        print("")
        
        while True:
            Retry = input("Do you want to draw again?(y/n): ")
            if Retry == "y":
                _ = os.system('clear')
                break
            elif Retry == "n":
                print("- Exiting...\n\n")
                exit()
            else:
                print("\nInput Error. Please enter(y/n)! ")

    else:
        UserInput = input("Input Error! Please enter 'y' or 'n' ")
        














