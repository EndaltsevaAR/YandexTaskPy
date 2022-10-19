"""
Description:
Игра PitCraft происходит в двумерном мире, который состоит из блоков
размером 1 на 1 метр. Остров игрока представляет собой набор различных
столбцов, состоящих из блока камня и окруженный морем. Над островом
прошел сильный дождь, который заполнил водой все низины, а не
поместившаяся в них вода стекла в море, не увеличив его уровень.
По ландшафту острова определить, сколько воды осталось после дождя в
низинах на острове
"""

def rain(columns):
    max_height_position = 0
    for i in range(len(columns)):
        if columns[i] > columns[max_height_position]:
            max_height_position = i
    answer = 0
    current_max = 0
    for i in range(max_height_position):
        if columns[i] > current_max:
            current_max = columns[i]
        answer += current_max - columns[i]
    current_max = 0
    for i in range(len(columns) - 1, max_height_position, -1):
        if columns[i] > current_max:
            current_max = columns[i]
        answer += current_max - columns[i]
    return answer


seq = list(map(int, input().split()))
# 3 1 4 3 5 1 1 3 1 example. Answer: 7
print(rain(seq))
