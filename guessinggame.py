import random
x=random.randint(1,100)
guess=0
print("The number is 1-100")
while(guess!=x):
    guess=int(input("What is your guess?"))
    if(guess==x):
        print("correct")
    if(guess>x):
        print("guess lower")
    if(guess<x):
        print("guess higher")
