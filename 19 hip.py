# -*- coding: utf-8 -*-

"""
https://contest.yandex.ru/contest/45468/problems/18

19. Хипуй
Ограничение времени	2 секунды
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
В этой задаче вам необходимо самостоятельно (не используя соответствующие классы и функции стандартной библиотеки) организовать структуру данных Heap для хранения целых чисел, над которой определены следующие операции: a) Insert(k) – добавить в Heap число k ; b) Extract достать из Heap наибольшее число (удалив его при этом).

Формат ввода
В первой строке содержится количество команд N (1 ≤ N ≤ 100000), далее следуют N команд, каждая в своей строке. Команда может иметь формат: “0 <число>” или “1”, обозначающий, соответственно, операции Insert(<число>) и Extract. Гарантируется, что при выполенении команды Extract в структуре находится по крайней мере один элемент.

Формат вывода
Для каждой команды извлечения необходимо отдельной строкой вывести число, полученное при выполнении команды Extract.

Пример 1
"""


class Heap:

    l = []

    def __init__(self):
        pass

    # Вспомогательная функция для замены двух индексов в списке
    def swap(self, i, j):
        self.l[i], self.l[j] = self.l[j], self.l[i]

    def pros_vniz(self):
        self.l[0] = self.l[-1]
        ind = 0
        while 2 + 2 * ind < len(self.l):
            m = 1 + 2 * ind
            if m + 1 < len(self.l) and self.l[m] < self.l[m + 1]:
                m += 1
            if self.l[ind] > self.l[m]:
                break
            self.swap(ind, m)
            ind = m
        self.l.pop()

    def pros_vverh(self):
        ind = len(self.l) - 1
        while ind > 0 and self.l[ind] > self.l[(ind - 1) // 2]:
            m = (ind - 1) // 2
            self.swap(ind, m)
            ind = m

    def insert(self, n):
        self.l.append(n)
        self.pros_vverh()

    def extract(self):
        """
        вывести и удалить наибольшее число
        """
        e = self.l[0]
        self.pros_vniz()
        return e


n = int(input())
l = [input() for _ in range(n)]

h = Heap()
for cmd in l:
    if cmd == '1':
        print(h.extract())

    else:
        _, n = cmd.split()
        h.insert(int(n))



