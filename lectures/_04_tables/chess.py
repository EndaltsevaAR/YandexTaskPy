"""
Description:
На шахматной доске N*N находятся M ладей (ладья бьет клетки на той же
горизонтали или вертикали до ближайшей занятой)

Определите, сколько пар ладей бьют друг друга.
Ладьи задаются парой чисел Х и У, обозначающих координаты клетки.
1<= N <= 10^9
0 <= M <= 2 * 10^5
"""
# сложность О(М)
# для ферзя нужны еще 2 словаря для i - j и i + j ля поиска по диагонали


def count_rocks(rocks):
    def add_rock(row_or_col, key):
        if key not in row_or_col:
            row_or_col[key] = 0
        row_or_col[key] += 1

    def count_pairs(row_or_col):
        pairs = 0
        for key in row_or_col:
            pairs += row_or_col[key] - 1
        return pairs

    rock_in_row = {}
    rocks_in_col = {}
    for row, col in rocks:
        add_rock(rock_in_row, row)
        add_rock(rocks_in_col, col)
    return count_pairs(rocks_in_col) + count_pairs(rock_in_row)

