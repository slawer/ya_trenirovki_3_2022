

"""

https://contest.yandex.ru/contest/45468/problems/30

30. НОП с восстановлением ответа
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Даны две последовательности, требуется найти и вывести их наибольшую общую подпоследовательность.

Формат ввода
В первой строке входных данных содержится число N – длина первой последовательности (1 ≤ N ≤ 1000).
Во второй строке заданы члены первой последовательности (через пробел) – целые числа, не превосходящие 10000 по модулю.

В третьей строке записано число M – длина второй последовательности (1 ≤ M ≤ 1000).
В четвертой строке задаются члены второй последовательности (через пробел) – целые числа,
не превосходящие 10000 по модулю.

Формат вывода
Требуется вывести наибольшую общую подпоследовательность данных последовательностей, через пробел.
"""


def pr_s():
    print()
    print(end='   ')
    for i in range(15):
        print(l2[i], end=' ')
    print('\n')
    for i in range(15):
        print(l1[i], end='  ')
        for j in range(15):
            print(dp[i][j], end=' ')
        print()


def pr():
    s, e = max(0, n - 40), max(0, m - 40)
    print()
    print(end='   ')
    for i in range(s, n):
        print(l1[i], end=' ')
    print('\n')
    for i in range(s, n):
        print(l2[i], end='  ')
        for j in range(e, m):
            print(dp[i][j], end=' ')
        print()


n = int(input())
l1 = [int(e) for e in input().split()]

m = int(input())
l2 = [int(e) for e in input().split()]

dp = [[0 for _ in range(m)] for _ in range(n)]

dp[0][0] = 1 if l1[0] == l2[0] else 0

for i in range(1, n):
    dp[i][0] = dp[i-1][0]
    if l1[i] == l2[0]:
        dp[i][0] = 1

for j in range(1, m):
    dp[0][j] = dp[0][j-1]
    if l1[0] == l2[j]:
        dp[0][j] = 1


for i in range(1, n):
    for j in range(1, m):
        if l1[i] == l2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

l = []
i, j = n-1, m-1

mm = max(dp[n-1])
is_c = False
i_m = -1
for i in range(n):
    if mm < dp[i][m-1]:
        mm = dp[i][m-1]
        is_c = True
        i_m = i

if mm != dp[i][j]:
    if is_c:
        i = i_m
    else:
        j = dp[n-1].index(mm)

while i > -1 and j > -1:
    if dp[i][j] == 0:
        break

    if i > 0 and dp[i-1][j] == dp[i][j]:
        i -= 1

    elif j > 0 and dp[i][j-1] == dp[i][j]:
        j -= 1

    else:
        l.append(l2[j])
        i -= 1
        j -= 1

print(" ".join(map(str, l[::-1])))


pr_s()
