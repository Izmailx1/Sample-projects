import random
import os

state_array = [
    """
     ------
     |    |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |    |
     | 
     |   
     |    
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   
     |   
     |     
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |   
     |    
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |   
     |   
    ----------
    """]

words = []
file = open("words.txt", 'r', encoding="utf8")
for i in file:
    words.append(i.strip())
errors_count = 0
cont = 'y'
while cont == 'Y' or cont == 'y':
    word = random.choice(words)
    guess_word = ''
    for i in range(len(word)):
        guess_word += '*'
    errors_count = 0
    entered_letters = []

    while errors_count < 7:

        print(f"Word: {guess_word}")
        while True:
            letter = input(f"Enter a letter: ")
            if letter in entered_letters:
                print(f"This letter has already been entered.\n")
            else:
                break

        entered_letters.append(letter)

        if letter in word:
            tmp = ''
            for i in range(len(word)):
                if letter == word[i]:
                    tmp += letter
                else:
                    tmp += guess_word[i]
            guess_word = tmp
            print(f"There is such a letter!\n")
        else:
            print(f"Wrong!")
            errors_count += 1
            print(state_array[errors_count - 1])

        if errors_count == 7:
            print(f"You lose( \n Word is \'{word}\'")
        elif '*' not in guess_word:
            print(f"You are win! \n Word is \'{word}\'")
            break

    cont = input(f"\nTo start over, enter y/Y: ")
    os.system('cls')
