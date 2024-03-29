

"""

https://contest.yandex.ru/contest/45468/problems/38

38. Блохи
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
На клеточном поле, размером NxM (2 ≤ N, M ≤ 250) сидит Q (0 ≤ Q ≤ 10000) блох в различных клетках. "Прием пищи"
блохами возможен только в кормушке - одна из клеток поля, заранее известная. Блохи перемещаются по полю странным
образом, а именно, прыжками, совпадающими с ходом обыкновенного шахматного коня. Длина пути каждой блохи до кормушки
определяется как количество прыжков. Определить минимальное значение суммы длин путей блох до кормушки или,
если собраться блохам у кормушки невозможно, то сообщить об этом. Сбор невозможен, если хотя бы одна из
блох не может попасть к кормушке.

Формат ввода
В первой строке входного файла находится 5 чисел, разделенных пробелом: N, M, S, T, Q. N, M - размеры доски
(отсчет начинается с 1); S, T - координаты клетки - кормушки (номер строки и столбца соответственно),
Q - количество блох на доске. И далее Q строк по два числа - координаты каждой блохи.

Формат вывода
Содержит одно число - минимальное значение суммы длин путей или -1, если сбор невозможен.

"""

from collections import defaultdict

# N M размеры
# S T координаты кормушки
N, M, S, T, Q = [int(e) for e in input().split()]

mm = 10**9
l = []
for i in range(1, Q+1):
    a, b = input().split()
    l.append((int(a), int(b)))


m = [[mm for _ in range(1, M + 2)] for _ in range(1, N + 2)]
m[S][T] = 0
st = [(S, T)]
while st:
    x, y = st.pop(0)
    d = m[x][y]
    t = []
    #print(len(st), sum([o.count(mm) for o in m]))

    if x - 2 > 0:
        if y - 1 > 0:
            t.append((x - 2, y - 1))
        if y + 1 <= M:
            t.append((x - 2, y + 1))

    if x + 2 <= N:
        if y - 1 > 0:
            t.append((x + 2, y - 1))
        if y + 1 <= M:
            t.append((x + 2, y + 1))

    if y - 2 > 0:
        if x - 1 > 0:
            t.append((x - 1, y - 2))
        if x + 1 <= N:
            t.append((x + 1, y - 2))

    if y + 2 <= M:
        if x - 1 > 0:
            t.append((x - 1, y + 2))
        if x + 1 <= N:
            t.append((x + 1, y + 2))

    for i, j in t:
        # if m[i][j] > d + 1:
        if m[i][j] == mm:

            if (i, j) not in st:
                st.append((i, j))
            m[i][j] = d + 1


cnt = 0
for x, y in l:
    if m[x][y] == mm:
        cnt = -1
        break
    cnt += m[x][y]

print(cnt)


#print(m)
