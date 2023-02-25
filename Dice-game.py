import random
import os

cont = 'y'
while cont == 'Y' or cont == 'y':

    players = int(input(f"Введите количество игроков: "))
    count = int(input(f"Введите количество костей, которые вы хотите бросить: "))
    sum_dict = {}
    for j in range(players):
        print(f"Игрок {j + 1} бросает кости")
        k = 0
        sum = [0] * players
        for i in range(count):
            k = random.randint(1, 6)
            sum[j] += k
            print(f"На кости {i + 1} выпало {k}")
        print(f"Сумма очков игрока {j + 1} = {sum[j]}\n")
        sum_dict[j] = sum[j]
    sum_dict = dict(sorted(sum_dict.items(), key=lambda item: item[1]))
    player_num = list(sum_dict.keys())
    sum = list(sum_dict.values())
    winners = []
    winners.append(player_num[-1])
    for i in range(players):
        if sum[players - 1] == sum[players - 2]:
            winners.append(player_num[players - 2])
            players -= 1
        else:
            break
    if len(winners) == 1:
        print(f"Победил игрок: {player_num[-1] + 1}!")
    else:
        print(f"Победители:")
        for i in winners:
            print(f"Игрок {i + 1}!")

    cont = input(f"Введите y/Y, чтобы бросить кости еще раз: ")
    os.system('cls')
