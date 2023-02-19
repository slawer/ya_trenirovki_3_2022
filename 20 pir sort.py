

"""
https://contest.yandex.ru/contest/45468/problems/20

20. Пирамидальная сортировка
Ограничение времени	2 секунды
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Отсортируйте данный массив. Используйте пирамидальную сортировку.

Формат ввода
Первая строка входных данных содержит количество элементов в массиве N, N ≤ 105. Далее задаются N целых чисел, не превосходящих по абсолютной величине 109.

Формат вывода
Выведите эти числа в порядке неубывания.

Пример 1
Ввод	Вывод
1
1
1
Пример 2
Ввод	Вывод
2
3 1
1 3
"""

f = [1, 3, 5, 7, 9]
s = [2, 4, 6, 8, 0]

f = [int(c) for c in input().split()]
s = [int(c) for c in input().split()]


def first_win(p, v):
    if p == 0:
        return v == 9
    if p == 9:
        return v != 0
    return p > v


for i in range(1, 10**6):
    if not f:
        print('second', i-1)
        exit(0)
    if not s:
        print('first', i-1)
        exit(0)
    kf = f.pop(0)
    ks = s.pop(0)
    # print(i)
    # print(kf, f)
    # print(ks, s)
    # print()
    if first_win(kf, ks):
        f.append(kf)
        f.append(ks)
    else:
        s.append(kf)
        s.append(ks)

print('botva')
