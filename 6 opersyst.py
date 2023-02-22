

"""
https://contest.yandex.ru/contest/45469/problems/6/

Васин жесткий диск состоит из M секторов. Вася последовательно устанавливал на него различные операционные системы
следующим методом: он создавал новый раздел диска из последовательных секторов, начиная с сектора номер ai и до
сектора bi включительно, и устанавливал на него очередную систему. При этом, если очередной раздел хотя бы по
одному сектору пересекается с каким-то ранее созданным разделом, то ранее созданный раздел «затирается», и
операционная система, которая на него была установлена, больше не может быть загружена.

Напишите программу, которая по информации о том, какие разделы на диске создавал Вася, определит, сколько в
итоге работоспособных операционных систем установлено и работает в настоящий момент на Васином компьютере.

Формат ввода
Сначала вводятся натуральное число M — количество секторов на жестком диске (1 ≤ M ≤ 109) и целое число
N — количество разделов, которое последовательно создавал Вася (0 ≤ N ≤ 1000).

Далее идут N пар чисел ai и bi, задающих номера начального и конечного секторов раздела (1 ≤ ai ≤ bi ≤ M).

Формат вывода
Выведите одно число — количество работающих операционных систем на Васином компьютере.

"""

"""
большое органичение - массив секторов не завести

значит нужно что-то придумать 

пометить затертую:
1- булева переменная в массиве
2 удаление из массива

эфффективно проверить пересечение отрезкой
a<=d and c<=b


в версии не лайт
хранить непересекающиеся отрезки
в него нужно добавить новый пришедший отрезок и звсавить
бинпоиском найти перекаемый -удалить - далее послежовательно найти пару след отрезков и удалить
и на один в лево проверить и удлалить если нужно


несколько вопросов
- как удалить из массива эффективно - из середины не удалить эффективно! - 
     можно например декартово область
     бинарное дерево - умеет все делать за н лог н и это общая сложность
- какая будет тогда сложность -  вроде н2 но нет - каждый только раз поэтому линейная
"""

# from collections import defaultdict

m = int(input())  # кол-во секторов
n = int(input())  # кол-во разделов
l = []  # нач и кон сектор
for _ in range(n):
    l.append([int(c) for c in input().split()])

act = []
for s, e in l:
    t = []
    for s1, e1 in act:
        if e1 < s:
            t.append((s1, e1))
        elif e < s1:
            t.append((s1, e1))

    act = t.copy()
    act.append((s, e))

print(len(act))
#print(act)

