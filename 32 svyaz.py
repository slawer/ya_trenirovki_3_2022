

"""

https://contest.yandex.ru/contest/45468/problems/32

32. Компоненты связности
Все языки	Python 3.6
Ограничение времени	2 секунды	5 секунд
Ограничение памяти	256Mb	256Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Дан неориентированный невзвешенный граф. Необходимо посчитать количество его компонент связности и вывести их.

Формат ввода
Во входном файле записано два числа N и M (0 < N ≤ 100000, 0 ≤ M ≤ 100000). В следующих M строках записаны по два
числа i и j (1 ≤ i, j ≤ N), которые означают, что вершины i и j соединены ребром.

Формат вывода
В первой строчке выходного файла выведите количество компонент связности. Далее выведите сами компоненты связности
в следующем формате: в первой строке количество вершин в компоненте, во второй - сами вершины в произвольном порядке.

"""


from collections import defaultdict

import sys
sys.setrecursionlimit(10000)

with open('input.txt', 'r') as f:
    i = f.readline()
    n, m = [int(e) for e in i.split(' ')]

    d = defaultdict(list)
    for _ in range(m):
        a, b = [int(e) for e in f.readline().split()]
        d[a].append(b)
        d[b].append(a)

if m == 0:
    print(n)
    for i in range(n):
        print(1)
        print(i+1)
    exit(0)

visited = [-1 for _ in range(n+1)]


def dfs(curr, comp):

    visited[curr] = comp
    for neib in d[curr]:
        nc = visited[neib]
        if nc == -1:
            dfs(neib, comp)


cnt = 0
for node in range(1, n+1):
    if visited[node] != -1:
        continue
    cnt += 1
    dfs(node, cnt)

cmp_node = defaultdict(list)
for i, e in enumerate(visited):
    if e == -1:
        cmp_node[-1].append(i)
        continue
    cmp_node[e].append(i)

print(cnt)
for i in cmp_node.pop(-1):
    if i == 0:
        continue
    print(1)
    print(i)

for l in cmp_node.values():
    print(len(l))
    for i in l:
        print(i, end=' ')
    print()

exit(0)


for c in range(1, cnt+1):
    # l = [str(i) for i, e in enumerate(visited) if e == c]
    cnt = 0
    for e in visited:
        if e != c:
            continue
        cnt += 1

    if cnt:
        print(cnt)
        for i, e in enumerate(visited):
            if e != c:
                continue
            print(i, end=' ')
        print()

    # print(len(l))
    # print(' '.join(l))


print()
print(visited)



