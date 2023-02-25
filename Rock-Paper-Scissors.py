import random
import os

cont = 'y'
while(cont == 'Y' or cont == 'y'):
    list = ['rock', 'paper', 'scissors']
    humanSelected = list[int(input(f"Enter 1 if rock, 2 if paper, 3 if scissors: ")) - 1]
    computerSelected = list[random.randint(0, 2)]
    print(f"\nYou have chosen a {humanSelected}")
    print(f"The computer chose a {computerSelected}\n")
    if humanSelected == computerSelected:
        print(f"Draw!")
    elif humanSelected == 'rock' and computerSelected == 'paper':
        print(f"You lose :(")
    elif humanSelected == 'paper' and computerSelected == 'rock':
        print(f"You have won!")
    elif humanSelected == 'rock' and computerSelected == 'scissors':
        print(f"You have won!")
    elif humanSelected == 'scissors' and computerSelected == 'rock':
        print(f"You lose :(")
    elif humanSelected == 'paper' and computerSelected == 'scissors':
        print(f"You lose :(")
    elif humanSelected == 'scissors' and computerSelected == 'paper':
        print(f"You have won!")

    cont = input(f"\nTo start over, enter y/Y: ")
    os.system('cls')
