

"""
https://contest.yandex.ru/contest/45468/problems/16

16. Очередь с защитой от ошибок
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Научитесь пользоваться стандартной структурой данных queue для целых чисел. Напишите программу, содержащую описание очереди и моделирующую работу очереди, реализовав все указанные здесь методы.

Программа считывает последовательность команд и в зависимости от команды выполняет ту или иную операцию. После выполнения каждой команды программа должна вывести одну строчку.

Возможные команды для программы:

push n
Добавить в очередь число n (значение n задается после команды). Программа должна вывести ok.

pop
Удалить из очереди первый элемент. Программа должна вывести его значение.

front
Программа должна вывести значение первого элемента, не удаляя его из очереди.

size
Программа должна вывести количество элементов в очереди.

clear
Программа должна очистить очередь и вывести ok.

exit
Программа должна вывести bye и завершить работу.

Перед исполнением операций front и pop программа должна проверять, содержится ли в очереди хотя бы один элемент. Если во входных данных встречается операция front или pop, и при этом очередь пуста, то программа должна вместо числового значения вывести строку error.

Формат ввода
Вводятся команды управления очередью, по одной на строке

Формат вывода
Требуется вывести протокол работы очереди, по одному сообщению на строке

Пример 1
Ввод	Вывод
push 1
front
exit
ok
1
bye
Пример 2
Ввод	Вывод
size
push 1
size
push 2
size
push 3
size
exit
0
ok
1
ok
2
ok
3
bye
Пример 3
Ввод	Вывод
push 3
push 14
size
clear
push 1
front
push 2
front
pop
size
pop
size
exit
ok
ok
2
ok
ok
1
ok
1
1
1
2
0
bye
"""


class Deq:
    _lim = 105
    f = _lim
    t = _lim
    l = [0 for _ in range(2*(_lim+1))]
    e = True

    def __init__(self):
        self.clear()

    def check_front(self):
        if self.f > 0:
            return
        t = [0 for i in range(self._lim)]
        for i in self.l:
            t.append(i)
        self.f += self._lim
        self.t += self._lim
        self.l = t

    def check_tail(self):
        if self.t < len(self.l) - 1:
            return
        for i in range(self._lim):
            self.l.append(0)

    def push_front(self, n):
        self.check_front()
        if not self.is_empty():
            self.f -= 1
        else:
            self.e = False
        self.l[self.f] = n

    def push_back(self, n):
        self.check_tail()
        if not self.is_empty():
            self.t += 1
        else:
            self.e = False
        self.l[self.t] = n

    def is_empty(self):
        return self.e

    def pop_front(self):
        if self.len() == 0:
            return 'error'
        r = self.l[self.f]
        if self.len() > 0:
            self.f += 1
        self.len()
        return r

    def pop_back(self):
        if self.len() == 0:
            return 'error'
        r = self.l[self.t]
        if self.len() > 0:
            self.t -= 1
        self.len()
        return r

    def front(self):
        if self.len() == 0:
            return 'error'
        return self.l[self.f]

    def back(self):
        if self.len() == 0:
            return 'error'
        return self.l[self.t]

    def len(self):
        if self.is_empty(): return 0
        l = self.t - self.f + 1
        if l == 0:
            self.e = False
        return l

    def clear(self):
        self.f = self._lim
        self.t = self._lim
        self.e = True


d = Deq()
l = []
while True:
    l.append(input())
    if l[-1] == 'exit':
        break

for s in l:
    if s == 'exit':
        break

    elif s.startswith('push'):
        _, n = s.split()
        d.push_back(n)
        print('ok')

    elif s.startswith('pop'):
        print(d.pop_front())

    elif s.startswith('front'):
        print(d.front())

    elif s.startswith('size'):
        print(d.len())

    elif s.startswith('clear'):
        d.clear()
        print('ok')

print('bye')





