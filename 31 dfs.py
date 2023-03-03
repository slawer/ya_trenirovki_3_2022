

"""

https://contest.yandex.ru/contest/45468/problems/31

31. Поиск в глубину
Все языки	Python 3.6
Ограничение времени	2 секунды	5 секунд
Ограничение памяти	256Mb	256Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Дан неориентированный граф, возможно, с петлями и кратными ребрами. Необходимо построить компоненту связности,
содержащую первую вершину.

Формат ввода
В первой строке записаны два целых числа N (1 ≤ N ≤ 103) и M (0 ≤ M ≤ 5 * 105) — количество вершин и ребер в графе.
В последующих M строках перечислены ребра — пары чисел, определяющие номера вершин, которые соединяют ребра.

Формат вывода
В первую строку выходного файла выведите число K — количество вершин в компоненте связности. Во вторую строку
выведите K целых чисел — вершины компоненты связности, перечисленные в порядке возрастания номеров.

"""

from collections import defaultdict
n, m = [int(e) for e in input().split()]


d = defaultdict(list)
for _ in range(m):
    a, b = [int(e) for e in input().split()]
    d[a].append(b)
    d[b].append(a)

visited = [-1 for _ in range(n+1)]


def dfs(curr, cmp):
    global cnt
    visited[curr] = cmp
    for neib in d[curr]:
        nc = visited[neib]
        if nc != cmp:
            cnt += 1
            dfs(neib, cmp)


cnt = 0
res = dfs(1, 1)

print(cnt + 1)
print(' '.join([str(i) for i, col in enumerate(visited) if col != -1]))


print(visited)



