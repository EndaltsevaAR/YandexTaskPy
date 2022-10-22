"""
Description:
Дана последовательность чисел длинной N.
Найти максимальное число в последовательности, если гарантированно, что она не пустая
"""

def max(seq):
    answer = seq[0]
    for i in range(1, len(seq)):
        if seq[i] > answer:
            answer = seq[i]
    return answer


seq = list(map(int, input().split()))
print(max(seq))
