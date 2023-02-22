

"""
https://contest.yandex.ru/contest/45469/problems/5/

На день рождения маленький Ипполит получил долгожданный подарок — набор дощечек с написанными на них
буквами латинского алфавита. Теперь-то ему будет чем заняться долгими вечерами, тем более что мама обещала
подарить ему в следующем году последовательность целых неотрицательных чисел, если он хорошо освоит этот набор.
Ради такого богатства Ипполит готов на многое.
Прямо сейчас юный исследователь полностью поглощён изучением хорошести строк. Хорошестью строки называется
количество позиций от 1 до L - 1 (где L — длина строки), таких, что следующая буква в строке является
следующей по алфавиту. Например, хорошесть строки "abcdefghijklmnopqrstuvwxyz" равна 25, а строки "abdc" — только 1.

Ипполит размышляет над решением закономерно возникающей задачи: чему равна максимально возможная хорошесть строки,
которую можно собрать, используя дощечки из данного набора? Вы-то и поможете ему с ней справиться.

Формат ввода
Первая строка ввода содержит единственное целое число N — количество различных букв в наборе (1 ≤ N ≤ 26).
Обратите внимание: в наборе всегда используются N первых букв латинского алфавита.

Следующие N строк содержат целые положительные числа ci — количество букв соответствующего
типа (1 ≤ ci ≤ 109). Таким образом, первое число означает количество букв "a", второе
число задаёт количество букв "b" и так далее.

Формат вывода
Выведите единственное целое число — максимально возможную хорошесть строки, которую можно собрать из имеющихся дощечек.

"""

"""
строятся столбики с кол-вом каждой букв идущих попорядку
и прибавляем в ответ 

ответ - минимум из кол-ва букв и следующих по алфафиту

"""

from collections import defaultdict

n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))

c = 0
f = True
while f:
    f = False
    st = -1
    m = 10**9
    for i in range(n-1):
        if l[i + 1] > 0 and l[i] > 0:
            if st == -1:
                st = i
            f = True
            m = min(m, min(l[i + 1], l[i]))
        elif st != -1:
            c += m * (i+1-st - 1)
            for j in range(st, i+1):
                l[j] -= m
            m = 0
            st = -1

    if st != -1:
        c += m * (n - st - 1)
        for j in range(st, n):
            l[j] -= m
        m = 0
        st = -1


print(c)
