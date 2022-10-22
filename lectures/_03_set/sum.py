"""Description:
Дана последовательность положительных чисел длиной N и число Х.
Нужно найти два различных сила A и В из последовательности, таких что А + В = Х
или вернуть пару 0,0, если таких пары чисел нет
"""


def long(nums, x):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == x:
                return nums[i], nums[j]
    return 0, 0


def solution_o_n(nums, x):
    prev_nums = set()
    for current_num in nums:
        if x - current_num in prev_nums:
            return current_num, x - current_num
        prev_nums.add(current_num)
    return 0, 0


seq = list(map(int, input().split()))
x = int(input())
print(solution_o_n(seq, x))
