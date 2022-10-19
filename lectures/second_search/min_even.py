"""
Description:
Дана последовательность чисел длинной N.
Найти минимальное четное число в последовательности или вывести -1, если такое
число не существует
"""


def min_even(seq):
    answer = -1
    flag = False
    for i in range(len(seq)):
        if seq[i] % 2 == 0 and (not flag or seq[i] < answer):
            answer = seq[i]
            flag = True
    return answer


seq = list(map(int, input().split()))
print(min_even(seq))
