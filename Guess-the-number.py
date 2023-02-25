import random
import os

cont = 'y'
while(cont == 'Y' or cont == 'y'):
    memberNum = int(input(f"Enter the number of participants: "))
    amountNum = int(input(f"Enter amount of numbers: "))
    numList = []
    for i in range(amountNum):
        numList.append(random.randint(0, 100))
    hiddenNum = numList[random.randint(0, amountNum - 1)]
    print(f"Numbers: {numList}")
    for i in range(memberNum):
        selectedNum = int(input(f"Member {i + 1}! Choose a number and enter it: "))
        if selectedNum == hiddenNum:
            print(f"You guessed the number!")
        else:
            print(f"You didn't guess the number :(")
    print(f"Hidden number is {hiddenNum}")
    cont = input(f"To start over, enter y/Y: ")
    os.system('cls')
