

"""
https://contest.yandex.ru/contest/45468/problems/20

20. Пирамидальная сортировка
Ограничение времени	2 секунды
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Отсортируйте данный массив. Используйте пирамидальную сортировку.

Формат ввода
Первая строка входных данных содержит количество элементов в массиве N, N ≤ 105. Далее задаются N целых чисел, не превосходящих по абсолютной величине 109.

Формат вывода
Выведите эти числа в порядке неубывания.

Пример 1
Ввод	Вывод
1
1
1
Пример 2
Ввод	Вывод
2
3 1
1 3
"""


class Node:

    val: int
    left: 'Node'
    right: 'Node'

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def add(root, val):
    e = Node(val)

    # сделать просеивание


    root.left = e
    return root


def tr(root):
    s = [root]
    m = []
    while s:
        c = s.pop()
        if not c:
            continue
        m.append(c.val)
        s.append(c.left)
        s.append(c.right)

    return m


n = int(input())
l = [int(c) for c in input().split()]

if not l:
    print([])
    exit(0)

root = Node(l[0])
for i in l[1:]:
    add(root, i)

m = tr(root)
print(m)




