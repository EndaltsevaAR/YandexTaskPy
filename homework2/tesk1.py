"""Description:
Два из трех
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Вам даны три списка чисел. Найдите все числа, которые встречаются хотя бы в двух из трёх списков.

Формат ввода
Во входных данных описывается три списка чисел. Первая строка каждого описания списка состоит из длины
списка n (1 ≤ n ≤ 1000). Вторая строка описания содержит список натуральных чисел, записанных через пробел.
Числа не превосходят 109.

Формат вывода
Выведите все числа, которые содержатся хотя бы в двух списках из трёх, в порядке возрастания. Обратите внимание,
что каждое число необходимо выводить только один раз."""

l1 = input()
s1 = set(map(int, input().split()))
l2 = input()
s2 = set(map(int, input().split()))
l3 = input()
s3 = set(map(int, input().split()))
answer = s1 & s2
merged12 = s1.union(s2)
answer = answer.union(merged12 & s3)
print(*sorted(answer))   # * помогает выводить без []