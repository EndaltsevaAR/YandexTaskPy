"""
Description:
Игрок в футбол обладает одной числовой характеристикой - профессионализмомю
Команда называется сплоченной, если профессионализм любого игрока не превосходит суммарный
профессионализм любых двух других игроков из команды. Команда может состоять из
любого количества игроков. Дана отсортированная последовательность чисел длиной N -
профессиональных игроков. Необходимо найти максимальный суммарный профессиональзм
сплоченной команды
"""

def best_team(players):
    best_sum = 0
    current_sum = 0
    last = 0
    for first in range(len(players)):
        while last < len(players) and (last == first or players[first] + players[first + 1] >= players[last]):
            current_sum += players[last]
            last += 1
        best_sum = max(current_sum, best_sum)
        current_sum -= players[first]
    return best_sum


seq = list(map(int, input().split()))
print(best_team(seq))
