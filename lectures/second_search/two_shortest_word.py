"""
Description:
Дана последовательность слов. Вывести два самых коротких слова через пробел
"""
import string


def short_words(words):
    min_len = len(words[0])
    for word in words:
        if len(word) < min_len:
            min_len = len(word)
    answer = []
    for word in words:
        if len(word) == min_len:
            answer.append(word)
    return " ".join(answer)


words = input().split()
print(short_words(words))

