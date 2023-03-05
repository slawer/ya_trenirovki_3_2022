

"""

https://contest.yandex.ru/contest/45468/problems/29

29. Кафе
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt

Около Петиного университета недавно открылось новое кафе, в котором действует следующая система скидок: при каждой
покупке более чем на 100 рублей покупатель получает купон, дающий право на один бесплатный обед (при покупке на
сумму 100 рублей и меньше такой купон покупатель не получает).

Однажды Пете на глаза попался прейскурант на ближайшие N дней. Внимательно его изучив, он решил, что будет обедать
в этом кафе все N дней, причем каждый день он будет покупать в кафе ровно один обед. Однако стипендия у Пети
небольшая, и поэтому он хочет по максимуму использовать предоставляемую систему скидок так, чтобы его суммарные
затраты были минимальны. Требуется найти минимально возможную суммарную стоимость обедов и номера дней,
 в которые Пете следует воспользоваться купонами.

Формат ввода
В первой строке входного файла записано целое число N (0 ≤ N ≤ 100). В каждой из последующих N строк записано
одно целое число, обозначающее стоимость обеда в рублях на соответствующий день. Стоимость — неотрицательное
целое число, не превосходящее 300.

Формат вывода
В первой строке выдайте минимальную возможную суммарную стоимость обедов. Во второй строке выдайте два числа
K1 и K2 — количество купонов, которые останутся неиспользованными у Пети после этих N дней и количество
использованных им купонов соответственно.

В последующих K2 строках выдайте в возрастающем порядке номера дней, когда Пете следует воспользоваться купонами.
Если существует несколько решений с минимальной суммарной стоимостью, то выдайте то из них, в котором значение
K1 максимально (на случай, если Петя когда-нибудь ещё решит заглянуть в это кафе). Если таких решений несколько,
выведите любое из них.
"""

"""

по оси дни и купоны

можем переходить только ото дня к дню
поели за купон - не потратили денег но потратили купон
едим за деньги - получаем купон и переходим ниже по у

инициализировать купоны бесконечностью

ходить по дням - по столбикам

но по строкам ходить быстрее

меняем оси местами

можно ли решить одномерной? - но не знаем будущего и будут ли дорогие обеды или дешевые - не знаем, поэтому не можем

итого
по горизонтали - купоны
по вертикали - дни
"""

m = 10**10
n = int(input())

l = [int(input()) for _ in range(n)]

dp = [[-1 for _ in range(n)] for _ in range(n)]

dp[0][0] = l[0]
for i in range(n):
    dp[i][0] = m

for i in range(n):
    for j in range(n):
        pass



print(dp)
print()
for i in range(n):
    for j in range(m):
        print('-' if dp[i][j] == -1 else 'x', end=' ')
    print()
