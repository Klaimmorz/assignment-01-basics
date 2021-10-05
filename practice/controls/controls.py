import math


def transpose(a):
    """Транспозиция матрицы"""
    s = []
    for i in range(len(a[0])):
        s.append(list())
        for j in range(len(a)):
            s[i].append(a[j][i])
    return s


def read_lines(input, print):
    """Количество непустых строк во вводе до первой пустой"""
    i = 0
    s = ''
    while True:
        s = input()
        if s == '':
            break
        else:
            i += 1
    print(i)


def min_prime(n):
    """Минимальный простой делитель числа"""
    if n % 2 == 0:
        return 2
    i = 3
    while n % i != 0 and i * i <= n:
        i += 2
    if i * i <= n:
        return i
    return n

def from_hexadecimal(s):
    """Перевод из шестнадцатеричной системы счисления"""
    s16 = "0123456789ABCDEF"
    acc = 0
    for a in s:
        p = s16.find(a.upper())
        if (p >= 16) | (p == -1):
            return None
        acc = acc * 16 + p
    return acc
