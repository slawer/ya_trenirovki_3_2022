

"""
https://contest.yandex.ru/contest/45468/problems/20

20. Пирамидальная сортировка
Ограничение времени	2 секунды
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
Отсортируйте данный массив. Используйте пирамидальную сортировку.

Формат ввода
Первая строка входных данных содержит количество элементов в массиве N, N ≤ 105. Далее задаются N целых чисел,
не превосходящих по абсолютной величине 109.

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


# возвращает левого потомка `A[i]`
def LEFT(i):
    return 2 * i + 1


# возвращает правого потомка `A[i]`
def RIGHT(i):
    return 2 * i + 2


# Вспомогательная функция для замены двух индексов в списке
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


# Рекурсивный алгоритм heapify-down. Узел с индексом `i` и
# два его прямых потомка нарушают свойство кучи
def heapify(A, i, size):
    # получает левый и правый потомки узла с индексом `i`
    left = LEFT(i)
    right = RIGHT(i)

    largest = i

    # сравнивает `A[i]` с его левым и правым дочерними элементами
    # и найти наибольшее значение
    if left < size and A[left] > A[i]:
        largest = left

    if right < size and A[right] > A[largest]:
        largest = right

    # поменяться местами с ребенком, имеющим большую ценность и
    # вызывает heapify-down для ребенка
    if largest != i:
        swap(A, i, largest)
        heapify(A, largest, size)


# Функция удаления элемента с наивысшим приоритетом (присутствует в корне)
def pop(A, size):
    # , если в куче нет элементов
    if size <= 0:
        return -1

    top = A[0]

    # заменить корень кучи последним элементом
    # списка
    A[0] = A[size - 1]

    # вызывает heapify-down на корневом узле
    heapify(A, 0, size - 1)

    return top


# Функция для выполнения пирамидальной сортировки в списке `A` размера `n`
def heapsort(A):
    # создает приоритетную очередь и инициализирует ее заданным списком
    n = len(A)

    # Build-heap: вызывать heapify, начиная с последнего внутреннего
    # Узел # вплоть до корневого узла
    i = (n - 2) // 2
    while i >= 0:
        heapify(A, i, n)
        i = i - 1

    # постоянно выталкивается из кучи, пока она не станет пустой
    while n:
        A[n - 1] = pop(A, n)
        n = n - 1


n = int(input())
l = [int(c) for c in input().split()]
heapsort(l)

print(' '.join([str(i) for i in l]))

exit(1)



#-------------------------------------


class Node:

    val: int
    left: 'Node'
    right: 'Node'

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def add(root, val):
    e = Node(val)

    # сделать просеивание

    root.left = e
    return root


def tr(root):
    s = [root]
    m = []
    while s:
        c = s.pop()
        if not c:
            continue
        m.append(c.val)
        s.append(c.left)
        s.append(c.right)

    return m


n = 5
l = [1, 2, 3, 4, 5]
l = [3, 1, 5, 4, 2]
# n = int(input())
# l = [int(c) for c in input().split()]


if not l:
    print([])
    exit(0)

'''
root = Node(l[0])
for i in l[1:]:
    add(root, i)

m = tr(root)
print(m)
'''


def pros(ind: int):
    while 1 + 2*ind < len(l):
        m = 1 + 2*ind
        if m + 1 < len(l) and l[m] > l[m+1]:
            m += 1
        if l[ind] < l[m]:
            break
        l[m], l[ind] = l[ind], l[m]
        ind = m


# Функция удаления элемента с наивысшим приоритетом (присутствует в корне)
def pop(A, size):
    # , если в куче нет элементов
    if size <= 0:
        return -1

    top = A[0]

    # заменить корень кучи последним элементом
    # списка
    A[0] = A[size - 1]

    # вызывает heapify-down на корневом узле
    pros(size - 1)

    return top


n = int(input())
l = [int(c) for c in input().split()]

i = len(l) // 2 - 1
while i >= 0:
    pros(i)
    i -= 1

while n:
    l[n - 1] = pop(l, n)
    n = n - 1

print(' '.join([str(i) for i in l]))


def min_heapify(A,k):
    l = left(k)
    r = right(k)
    if l < len(A) and A[l] < A[k]:
        smallest = l
    else:
        smallest = k
    if r < len(A) and A[r] < A[smallest]:
        smallest = r
    if smallest != k:
        A[k], A[smallest] = A[smallest], A[k]
        min_heapify(A, smallest)


def left(k):
    return 2 * k + 1


def right(k):
    return 2 * k + 2


def build_min_heap(A):
    n = int((len(A)//2)-1)
    for k in range(n, -1, -1):
        min_heapify(A, k)


build_min_heap(l)
print(l)



