
color = "blue"
user_choice = ""
count = 0

while user_choice != color:
    user_choice = input("What color am I thinking of?: ")
    count = count + 1

#print("You got it! It took you", count, "guesses")

if count == 1:
    print("You got it! It took you", count, "guess")
else:
    print("You got it! It took you", count, "guesses")


