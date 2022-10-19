"""
Description:
Дана строка (возможно, пустая), состоящая из букв A-Z:
AAAABBBCCXYZDDD...
Нужно написать функцию RLE, которая на выходе даст строку вида:
A4B3C2XYZD3 и сгенерирует ошибку, если на вход пришла невалидная строка.
Если символ встречается 1 раз, цифра не ставится после нее, если символ
встречается более 1 раза подряд, после буквы ставится количество повторений
"""

def rle(seq):
    def pack(seq, number_repead):
        if number_repead > 1:
            return seq + str(number_repead)
        return seq

    last_symb = seq[0]
    last_position = 0
    answer = []
    for i in range(len(seq)):
        if seq[i] != last_symb:
            answer.append(pack(last_symb, i - last_position))
            last_position = i
            last_symb = seq[i]
    answer.append(pack(seq[last_position], len(seq) - last_position))
    return "".join(answer)
