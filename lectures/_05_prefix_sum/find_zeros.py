"""Дана последовательность числе длиной N и M запросов.
Запросы: "Сколько нулей на полуинтервале [L, R)?
Сложность O(N + M)
"""


def make_prefix_zeros(nums):
    prefix_zeros = [0] * (len(nums) + 1)
    for i in  range(1, len(nums) + 1):
        if nums[i-1] == 0:
            prefix_zeros[i] = prefix_zeros[i-1] + 1
        else:
            prefix_zeros[i] = prefix_zeros[i-1]
    return prefix_zeros


def count_zeros(prefix_zeros, l, r):
    return prefix_zeros[r] - prefix_zeros[l]


seq = list(map(int, input().split()))
left = int(input())
right = int(input())
prefix = make_prefix_zeros(seq)
print(count_zeros(prefix, left, right))
