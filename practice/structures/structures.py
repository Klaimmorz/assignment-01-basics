def kth(a, k):
    """k-е по величине значение в массиве"""
    a.sort()
    return a[k-1]


def head_tail(a, k):
    """Первые и последние k элементов в массиве"""
    return a[:k] + a[len(a)-k:]


def filter_sort(a, c):
    """Отсортировать копию массива, удалив строки с символом c"""
    g = a
    g.sort()
    i = 0
    flag = 0
    while i < len(g):
        print(i)
        for j in g[i]:
            if j == c:
                flag += 1
        if flag > 0:
            g.remove(g[i])
            flag = 0
        else:
            i += 1
    return g



def build_dict(keys, values):
    """Построить словарь по набору ключей и значений"""
    k = dict(zip(keys, values))
    return k


def compare_contents(a1, a2):
    """Проверка наборов элементов на совпадение"""
    for i in a1:
        if a2.count(i) == 0:
            return False
    for i in a2:
        if a1.count(i) == 0:
            return False
    return True

