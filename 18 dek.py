# -*- coding: utf-8 -*-

"""
https://contest.yandex.ru/contest/45468/problems/18

18. Дек с защитой от ошибок
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Научитесь пользоваться стандартной структурой данных deque для целых чисел.  Напишите программу, содержащую
описание дека и моделирующую работу дека, реализовав все указанные здесь методы. Программа считывает
последовательность команд и в зависимости от команды выполняет ту или иную операцию. После выполнения каждой
команды программа должна вывести одну строчку.

Возможные команды для программы:

push_front n
Добавить (положить) в начало дека новый элемент. Программа должна вывести ok.

push_back n
Добавить (положить) в конец дека новый элемент. Программа должна вывести ok.

pop_front
Извлечь из дека первый элемент. Программа должна вывести его значение.

pop_back
Извлечь из дека последний элемент. Программа должна вывести его значение.

front
Узнать значение первого элемента (не удаляя его). Программа должна вывести его значение.

back
Узнать значение последнего элемента (не удаляя его). Программа должна вывести его значение.

size
Вывести количество элементов в деке.

clear
Очистить дек (удалить из него все элементы) и вывести ok.

exit
Программа должна вывести bye и завершить работу.

Гарантируется, что количество элементов в деке в любой момент не превосходит 100. Перед исполнением операций pop_front,
pop_back, front, back программа должна проверять, содержится ли в деке хотя бы один элемент. Если во входных данных
встречается операция pop_front, pop_back, front, back, и при этом дек пуст, то программа должна вместо числового
значения вывести строку error.

Формат ввода
Вводятся команды управления деком, по одной на строке.

Формат вывода
Требуется вывести протокол работы дека, по одному сообщению на строке

Пример 1
Ввод	Вывод
push_back 1
back
exit
ok
1
bye
"""


class Dek:
    _lim = 102
    f = _lim
    t = _lim
    l = [0 for _ in range(2*(_lim+1))]
    e = True

    def __init__(self):
        self.clear()

    def push_front(self, n):
        if not self.is_empty():
            self.f -= 1
        else:
            self.e = False
        self.l[self.f] = n

    def push_back(self, n):
        if not self.is_empty():
            self.t += 1
        else:
            self.e = False
        self.l[self.t] = n

    def is_empty(self):
        return self.e

    def pop_front(self):
        if self.is_empty():
            return 'error'
        r = self.l[self.f]
        self.f += 1
        return r

    def pop_back(self):
        if self.is_empty():
            return 'error'
        r = self.l[self.t]
        self.t -= 1
        return r

    def front(self):
        if self.is_empty():
            return 'error'
        return self.l[self.f]

    def back(self):
        if self.is_empty():
            return 'error'
        return self.l[self.t]

    def len(self):
        if self.is_empty(): return 0
        return self.t - self.f + 1

    def clear(self):
        self.f = 100
        self.t = 100
        self.e = True


d = Dek()
l = []
while True:
    l.append(input())
    if l[-1] == 'exit':
        break

for s in l:
    if s == 'exit':
        break

    elif s.startswith('push_front'):
        _, n = s.split()
        d.push_front(n)
        print('ok')

    elif s.startswith('push_back'):
        _, n = s.split()
        d.push_back(n)
        print('ok')

    elif s.startswith('pop_front'):
        print(d.pop_front())

    elif s.startswith('pop_back'):
        print(d.pop_back())

    elif s.startswith('front'):
        print(d.front())

    elif s.startswith('back'):
        print(d.back())

    elif s.startswith('size'):
        print(d.len())

    elif s.startswith('clear'):
        d.clear()
        print('ok')

print('bye')
