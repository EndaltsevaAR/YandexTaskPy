""" Дана последовательность  чисел длиной N.
Необходимо найти количество отрезвок с нулевой суммой"""


def count_prefix_sum(nums):
    prefix_sum_value = {0: 1}   # словарь. Ключ - сумма, валью - частота появления
    current_sum = 0
    for num in nums:
        current_sum += num
        if current_sum not in prefix_sum_value:
            prefix_sum_value[current_sum] = 0
        prefix_sum_value[current_sum] += 1
    return prefix_sum_value


def count_zero_len(prefix):
    count = 0
    for curr in prefix:
        count_sum = prefix[curr]
        count += count_sum * (count_sum -1) // 2
    return count


seq = list(map(int, input().split()))
prefix = count_prefix_sum(seq)
print(count_zero_len(prefix))