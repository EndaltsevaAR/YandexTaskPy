"""Пусть у нас есть массив nums из N чисел и есть необходимость
отвечать на запросы "Чему равна сумма элементов на
полуинтервале [L, R)?

Метод решения: создать еще один массив с размером плюс 1.
В первой ячейке ноль, в следующих - значение предыдущей ячейки этого массива
и предыдущей ячейки основного массива.
Нужно иметь ввиду риск переполнения.
Имеет смысл, если запросов больше одного"""


def make_prefix_sum(nums):
    prefix_sum = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
    return prefix_sum


def rsq(prefix_sum, l, r):
    return prefix_sum[r] - prefix_sum[l]


seq = list(map(int, input().split()))
left = int(input())
right = int(input())
prefix = make_prefix_sum(seq)
print(rsq(prefix, left, right))

