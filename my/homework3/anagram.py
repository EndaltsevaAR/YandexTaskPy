"""
Description:
Анаграмма?
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Задано две строки, необходимо проверить, является ли одна анаграммой другой. Анаграммами называются строки,
состоящие из одних и тех же букв.

Формат ввода
Строки состоят из маленьких латинских букв, их длина не превосходит 100000. Каждая записана в отдельной строке.

Формат вывода
Выведите YES если одна из строк является анаграммой другой и NO в противном случае.
"""


def is_anagram(line1, line2):
    return sorted(line1) == sorted(line2)   # O(N * log)


line1 = input()
line2 = input()
if is_anagram(line1, line2):
    print("YES")
else:
    print("NO")
