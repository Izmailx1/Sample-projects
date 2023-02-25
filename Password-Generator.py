import random
import os

symbols = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,/';!*&$%#()_=+-^<>:\""
cont = 'y'

while cont == 'Y' or cont == 'y':
    password = ''
    lenght = int(input(f"Enter a password lenght: "))
    for i in range(lenght):
        password += random.choice(symbols)
    print(f"Generated password: {password}")
    cont = input(f"Type (y/Y) if you want to generate another password: ")
    os.system('cls')
