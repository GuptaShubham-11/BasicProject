# Guess The Number For Program

import random

target=random.randint(1,100)

while True:
    userChoise=int(input("Guess The Number:"))
    if(userChoise==target):
        print("You Are Winner Of The Game.")
        break
    elif(userChoise>target):
        print("Your Guess is Bigger Then The Target Number!")
    else:
        print("Your Guess is Smaller Then The Target Number!")

print("____Game Over____")