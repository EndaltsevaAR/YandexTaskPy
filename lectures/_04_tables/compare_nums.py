"""
Description:
Дано два числа Х и У без ведущих нулей.
Необходимо проверить, можно ли получить первое из второго перестановкой цифр
"""

def solution(x, y):
    def count_digits(number):
        digits = [0] * 10
        while number > 0:
            last_digit = number % 10
            digits[last_digit] += 1
            number //= 10
        return digits

    digits_x = count_digits(x)
    digits_y = count_digits(y)
    for digit in range(10):
        if digits_x[digit] != digits_y[digit]:
            return False
    return True


x_num = int(input())
y_num = int(input())
print(solution(x_num, y_num))