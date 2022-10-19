"""
Description:
Дана последовательность чисел длинной N.
Найти первое (левое) вхождение положительного числа Х в нее
или вывести -1, если число Х не встречалось
"""

def search(seq, x):
    answer = -1
    for i in range(len(seq)):
        if answer == -1 and seq[i] == x:
            answer = i
    return answer


seq = list(map(int, input().split()))
x = int(input())
print(search(seq, x))
