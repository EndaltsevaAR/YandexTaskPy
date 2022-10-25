"""
Description:
Дана отсортированная последовательность чисел длиной N и число K.
Необходимо найти количество пар чисел А, В, таких, что В - А > K
O(N)
"""
def long_n2_solution(nums, k):
    count = 0
    for first in range(len(nums)):
        for last in range(first + 1, len(nums)):
            if nums[last] - nums[first] > k:
                count += 1
    return count


def solution_two_pointers(nums, k):
    count = 0
    right = 0
    for left in range(len(nums)):
        while right < len(nums) and (nums[right] - nums[left]) <= k:
            right += 1
        count += len(nums) - right
    return count


seq = list(map(int, input().split()))
x = int(input())
print(long_n2_solution(seq, x))
print(solution_two_pointers(seq, x))
