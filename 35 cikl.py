

"""

https://contest.yandex.ru/contest/45468/problems/35

35. Поиск цикла
Все языки	Python 3.6
Ограничение времени	2 секунды	5 секунд
Ограничение памяти	256Mb	256Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

Дан неориентированный граф. Требуется определить, есть ли в нем цикл, и, если есть, вывести его.

Формат ввода
В первой строке дано одно число n — количество вершин в графе ( 1 ≤ n ≤ 500 ). Далее в n строках задан сам
граф матрицей смежности.

Формат вывода
Если в иcходном графе нет цикла, то выведите «NO». Иначе, в первой строке выведите «YES», во второй строке выведите
число k — количество вершин в цикле, а в третьей строке выведите k различных чисел — номера вершин, которые
принадлежат циклу в порядке обхода (обход можно начинать с любой вершины цикла). Если циклов несколько,
то выведите любой.




"""

from collections import defaultdict

import sys
sys.setrecursionlimit(10000)


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

visited = [-1 for _ in range(n+1)]
meeted = []


def dfs(curr, root):

    visited[curr] = 1
    for neib in d[curr]:
        nc = visited[neib]
        # meeted.append(curr)
        if root and root == neib:
            continue
        if nc == 1:
            meeted.append(neib)
            return 0
        elif nc == 2:
            continue

        if 0 == dfs(neib, curr):
            meeted.append(neib)
            return 0

    visited[curr] = 2
    #if curr in meeted:
    #    meeted.remove(curr)
    return 1


for node in range(1, n+1):
    if visited[node] != -1:
        continue
    meeted = []
    if dfs(node, None) == 0:
        print('YES')

        if meeted[0] in meeted[1:]:
            ind = meeted[1:].index(meeted[0])
            if ind > -1:
                meeted = meeted[:ind+1]
        print(len(meeted))
        for e in meeted:
            print(e, end=" ")
        exit(0)

print('NO')
exit(0)


for i in range(len(meeted)-1, -1, -1):
    print(meeted[i], end=' ')
print()


print(visited)
print(d)
print(m)



