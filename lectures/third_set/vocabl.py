"""
Description:
Дан словать из N слов, длина каждого не превосходит K.
В записи каждого из M слов текста (каждое длиной до К)
может быть пропущена 1 буква. Для каждого слова сказать, входит ли оно
(возможно с 1 пропущенной буквой) в словарь
"""
# solution for O(NK^2 + M)
# добавляем в сет все варианты слов с пропущенной одной буквой - то есть К вариантов для одного слова


def word_in_dict(dicts, text):
    good_words = set(dicts)
    for word in dicts:
        for delete_pos in range(len(word)):
            good_words.add(word[:delete_pos] + word[delete_pos + 1:])
    answer = []
    for word in text:
        if word in good_words:
            answer.append(word)
    return answer


dictionary = input().split()
texts = input().split()
print(word_in_dict(dictionary, texts))
