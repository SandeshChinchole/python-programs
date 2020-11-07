
# you prompt the player with “What color am I thinking of?” and you
# see how many guesses it takes the player to guess it.

import random

colors = ["red", "blue", "green", "yellow"]

computer_choice = random.choice(colors)

user_choice = input("What color am I thinking of?: ")

if computer_choice == user_choice:
    print("The choices match")
else:
    print("The choices don't match")
