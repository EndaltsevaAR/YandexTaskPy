"""
Description:
Юра решил подготовиться к собеседованию в Яндексе. Он
выбрал на сайте leetcode N задач. В первый день Юра решил K
задач, а в каждый следующий день Юра решал на одну задачу больше, чем в предыдущий
день. Определите, сколько дней уйдет у Юры на подготовку к
собеседованию
Решение: left = 0, right = N - количество задач
"""


def find_days(n, k):
    left = 0
    right = n
    while left < right:
        m = (left + right) // 2   # количество дней
        if (2 * k + m - 1) * m / 2 >= n:
            right = m
        else:
            left = m + 1
    return left
