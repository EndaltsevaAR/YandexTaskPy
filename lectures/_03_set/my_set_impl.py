"""Реализовать собственную имплементацию множества и основных команд:
добавление элемента, удаление элемента, и проверка, содержит ли множество этот
элемент"""
setsize = 10
myset = [[] for _ in range(setsize)]

def add(x):
    # x % setsize : хеш функция
    myset[x % setsize].append(x)


def find(x):
    for now in myset[x % setsize]:
        if now == x:
            return True
    return False


def delete(x):
    xlist = myset[x % setsize]
    for i in range(len(xlist)):
        if xlist[i] == x:
            xlist[i] = xlist[len(xlist) - 1]
            xlist.pop()
            return
