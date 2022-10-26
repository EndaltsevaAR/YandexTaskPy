"""Время поиска O(log)"""
"""Левый бинпоиск - первое подходящее значение"""


def l_bin_search(left, right, check, check_params):
    while left < right:  #выход из цикла, когда они будут равны
        m = (left + right) // 2   # округление в меньшую сторону
        if check(m, check_params):   # функция check передается в параметрах
            right = m     # когда все хорошо, мы двигаем правую границу
        else:
            left = m + 1   # когда все плохо, мы двигаем левую границу правее на один чем точка проверки
    return left


"""Правый бинпоиск - последнее подходящее значение"""


def r_bin_search(left, right, check, check_params):
    while left < right:
        m = (left + right + 1) // 2  # округляем в большую сторону
        if check(m, check_params):
            left = m   # если все хорошо, мы двигаем левую границу
        else:
            right = m - 1  # если все плохо, мы двигаем правую границу левее точки проверки
    return left
