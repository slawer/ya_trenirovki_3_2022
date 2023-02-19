

"""
https://contest.yandex.ru/contest/45468/problems/2/

Красотой строки назовем максимальное число идущих подряд одинаковых букв. (красота строки abcaabdddettq равна 3)
Сделайте данную вам строку как можно более красивой, если вы можете сделать не более k операций замены символа.

В первой строке записано одно целое число k (0 ≤ k ≤ 10**9)
Во второй строке дана непустая строчка S (|S| ≤ 2 ⋅ 10**5). Строчка S состоит только из маленьких латинских букв.

"""

from collections import defaultdict

#k = int(input())
#s = input()

k = 2
s = 'abcaz'

if len(s) <= k:
    print(len(s))
    exit(0)

d = defaultdict(list)
c = 1
l = []
for i in range(1, len(s)):
    if s[i-1] == s[i]:
        c += 1
    else:
        l.append((s[i-1], c))
        c = 1

l.append((s[-1], c))
print(l)




