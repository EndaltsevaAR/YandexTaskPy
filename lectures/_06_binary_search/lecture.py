"""
Description:
Михаил читает лекции по алгоритмам. За кадром стоит доска размером
W * H сантиметров. Михаилу нужно разместить на доске N квадртаных
стикеров со шпаргалками, при этом длина стороны стикера в сантиметрах должна быть
целым числом.
Определите максимальную длину стикера, чтобы все стикеры поместились на доске.
"""


def right_search(w, h, n):
    left = 0
    right = max(w, h)
    while left != right:
        m = (left + right + 1) // 2
        if (w // m) * (h // m) >= n:
            left = m
        else:
            right = m - 1
    return left


w = int(input())
h = int(input())
n = int(input())
print(right_search(w, h, n))

