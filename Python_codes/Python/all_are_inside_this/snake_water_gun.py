import random

computer = random.choice([-1, 0, 1])
yourinput = input("enter snake or water or gun\n").lower()

conversiondict={
    "snake":-1,
    "water":0,
    "gun":1
}
reverseconversiondict={
    -1:"snake",
    0:"water",
    1:"gun"
}
yourchoice=conversiondict[yourinput]
print(f"your entered {yourinput} and computer did {reverseconversiondict[computer]}")

if computer == yourchoice:
    print("It's a Draw!")

elif computer == -1 and yourchoice == 0:
    print("You lost!")   # Snake drinks water

elif computer == -1 and yourchoice == 1:
    print("You win!")    # Gun kills snake

elif computer == 0 and yourchoice == -1:
    print("You win!")    # Snake drinks water

elif computer == 0 and yourchoice == 1:
    print("You lost!")   # Water beats gun

elif computer == 1 and yourchoice == -1:
    print("You lost!")   # Gun kills snake

elif computer == 1 and yourchoice == 0:
    print("You win!")    # Water beats gun



    # another ways 

    