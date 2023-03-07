

"""

https://contest.yandex.ru/contest/45468/problems/37

37. Путь в графе
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
В неориентированном графе требуется найти минимальный путь между двумя вершинами.

Формат ввода
Первым на вход поступает число N – количество вершин в графе (1 ≤ N ≤ 100). Затем записана матрица смежности
(0 обозначает отсутствие ребра, 1 – наличие ребра). Далее задаются номера двух вершин – начальной и конечной.

Формат вывода
Выведите сначала L – длину кратчайшего пути (количество ребер, которые нужно пройти), а потом сам путь.
Если путь имеет длину 0, то его выводить не нужно, достаточно вывести длину.

Необходимо вывести путь (номера всех вершин в правильном порядке). Если пути нет, нужно вывести -1.

"""

import sys
sys.setrecursionlimit(10000)

from collections import defaultdict


n = [int(e) for e in input().split()][0]

m = [[False for _ in range(n+1)] for _ in range(n+1)]
d = defaultdict(list)

for i in range(1, n+1):
    t = input().split()
    for j in range(1, n+1):
        is_r = t[j-1] == '1'
        m[i][i] = is_r
        if not is_r:
            continue
        #if i in d[j]:
        #    continue
        if j not in d[i]:
            d[i].append(j)
        if i not in d[j]:
            d[j].append(i)
s, e = [int(e) for e in input().split()]

visited = [-1 for _ in range(n+1)]
prev = [-1 for _ in range(n+1)]


def bfs(st):
    s = [st]
    dist[st] = 0
    while s:
        c = s.pop()
        r = dist[c]
        for n in d.get(c, []):
            if dist[n] == -1:
                s.append(n)
                prev[n] = c
                dist[n] = r + 1

            else:
                if r + 1 < dist[n]:
                    dist[n] = r + 1
                    prev[n] = c
                    s.append(n)


dist = [-1 for _ in range(n + 1)]
bfs(s)

print(dist[e])

if dist[e] not in [-1, 0]:
    i = e
    p = [e]
    while i != s:
        i = prev[i]
        p.append(i)

    print(' '.join(map(str, p[::-1])))



print(d)
print(dist)
print(prev)





