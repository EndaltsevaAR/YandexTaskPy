"""
Description:
Дана строка. Найти в ней самый часто встречающийся символ. Если несколько символов
встречаются одинаково часто, то можно вывести любой
"""


word = input()
answer = ''
answer_int = 0
symb_dict = {}
for letter in word:
    if letter not in symb_dict:
        symb_dict[letter] = 0
    symb_dict[letter] += 1
    if symb_dict[letter] > answer_int:
        answer_int = symb_dict[letter]
        answer = letter
print(answer)
