# Guess The Number For Program

import random

target=random.randint(1,1000)

while True:
    userChoise=input("Guess The Number OR Quit for type 'Q':")
    if (userChoise=="Q"):
        print("_____QUIT_____")
        break
    userChoise=int(userChoise)
    if(userChoise==target):
        print("You Are Winner Of The Game.")
        break
    elif(userChoise>target):
        print("Your Guess is Bigger Then The Target Number!")
    else:
        print("Your Guess is Smaller Then The Target Number!")

print("____Game Over____")