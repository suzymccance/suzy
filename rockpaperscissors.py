import random
print("1 is scissors, 2 is paper, and 3 is rock")
rps=input("What is your move")
x=random.randint(1,3)
spr=""
if(x==1):
    print("Its scissors")
    spr="scissors" 
if(x==2):
    print("its rock")
    spr="rock"
if(x==3):
    print("its paper")
    spr="paper"

if(rps=="rock" and spr=="scissors"):
    print("Person win")
if(rps=="sccisors" and spr=="paper"):
    print("Person win")
if(rps=="paper" and spr=="rock"):
    print("I win")



if(rps=="rock" and spr=="paper"):
    print("Computer wins")
if(rps=="scissorcs" and spr=="rock"):
    print("computer wins")
if(rps=="paper" and spr=="scissors"):
    print("computer wins")


if(rps=="rock" and spr=="rock"):
    print("its a tie")
if(rps=="scissors"and spr=="scissors"):
    print("its a tie")
if(rps=="paper" and spr=="paper"):
    print("its a tie")