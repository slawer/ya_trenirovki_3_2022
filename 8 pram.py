

"""
https://contest.yandex.ru/contest/45469/problems/8/

На клетчатой плоскости закрашено K клеток. Требуется найти минимальный по площади прямоугольник,
со сторонами, параллельными линиям сетки, покрывающий все закрашенные клетки.

Формат ввода
Во входном файле, на первой строке, находится число K (1 ≤ K ≤ 100).
На следующих K строках находятся пары чисел Xi и Yi – координаты закрашенных клеток (|Xi|, |Yi| ≤ 109).

Формат вывода
Выведите в выходной файл координаты левого нижнего и правого верхнего углов прямоугольника.

"""

"""
самая простая 

просто найти минимуми и максимумы по осям
"""

from collections import defaultdict

m = 10**9
k = int(input())
t, b, r, l = -1, m, -1, m
for _ in range(k):
    x, y = [int(c) for c in input().split()]
    t = max(t, x)
    b = min(b, x)

    r = max(r, y)
    l = min(l, y)

print(b, l, t, r)
