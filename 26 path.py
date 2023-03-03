

"""

https://contest.yandex.ru/contest/45468/problems/26

26. Самый дешевый путь
Ограничение времени	1 секунда
Ограничение памяти	256Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

 записано некоторое число. Изначально игрок находится в левой верхней клетке.

 За один ход ему разрешается перемещаться  в соседнюю клетку либо вправо, либо вниз
 (влево и вверх перемещаться запрещено).

 При проходе через клетку с игрока берут столько килограммов еды, какое число записано в этой клетке
 (еду берут также за первую и последнюю клетки его пути).

Требуется найти минимальный вес еды в килограммах, отдав которую игрок может попасть в правый нижний угол.

"""


n, m = [int(e) for e in input().split()]

l = [[-1 for _ in range(m)] for _ in range(n)]
dp = [[-1 for _ in range(m)] for _ in range(n)]

for i in range(n):
    t = input().split()
    for j in range(m):
        l[i][j] = int(t[j])
        dp[i][j] = -1

dp[0][0] = l[0][0]

s = [(0, 0)]

while s:
    i, j = s.pop(0)
    if i + 1 < n and (i+1, j) not in s:
        s.append((i+1, j))
    if j + 1 < m and (i, j+1) not in s:
        s.append((i, j+1))
    if dp[i][j] != -1:
        continue
    t = []
    if i - 1 >= 0:
        if dp[i-1][j] != -1:
            t.append(dp[i-1][j])
        elif (i, j) not in s:
            s.append((i, j))
            continue
    if j - 1 >= 0:
        if dp[i][j-1] != -1:
            t.append(dp[i][j-1])
        elif (i, j) not in s:
            s.append((i, j))
            continue
    if not t:
        continue
    dp[i][j] = min(t) + l[i][j]
    # print(i, j, t, l[i][j], dp[i][j])

print(dp[n-1][m-1])


print()
for i in range(n):
    for j in range(m):
        print(dp[i][j], end=' ')
    print()

