

"""
https://contest.yandex.ru/contest/45468/problems/21

21. Три единицы подряд
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
По данному числу N определите количество последовательностей из нулей и единиц длины N, в которых никакие три единицы не стоят рядом.

Формат ввода
Во входном файле написано натуральное число N, не превосходящее 35.

Формат вывода
Выведите количество искомых последовательностей. Гарантируется, что ответ не превосходит 231-1.

Пример
Ввод	Вывод
1
2

"""


def run1():
    c = 0
    for i in range(2**n):
        if '111' not in bin(i):
            c += 1
    return c


def run():

    dp = [0 for _ in range(max(4, n+1))]
    dp[0] = 1
    dp[1] = 2
    dp[2] = 4

    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    return dp[n]


n = int(input())
print(run())


for n in range(15):
    c = run()
    print(n, c)

