e=6
x=7
q="-"
a=-1
number1=input("what is the first number to the equation?")
operation=input("what is the operation to the equation")
number2=input("what is the second number to the equation?")
equals=input("type the equal sign")
answer=input("type answer here")

if(number1==e):
    print(e,"✔️")

else:
    if(number1==x):
        print("🚫")
    if(number1==a):
        print("🚫")






if(operation==q):
    print(q,"✔️")
if(q!=operation):
    print(q,"⬛")



if(number2==x):
    print(x,"✔️")
elif(number2==e):
    print(e,"🚫")


print("=")


if(answer==a):
    print(a,"✔️")
elif(answer==x):
    print(answer,"🚫")   
elif(answer==e):
    print(answer,"🚫")
else:
    print(answer,"⬛")