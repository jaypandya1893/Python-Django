import random

num=random.randint(1,20)

while True:
    guess=int(input("Guess the number between 1 to 20:  "))

    if guess==num:
        print("You Guessed a correct number")
        break
    elif guess>num:
        print("You Guessed a Greater number")
    elif guess<num:
        print("You Guessed a Smaller number")
