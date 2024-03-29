

"""

https://contest.yandex.ru/contest/45468/problems/24

24. Покупка билетов
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
За билетами на премьеру нового мюзикла выстроилась очередь из N человек, каждый из которых хочет купить 1 билет.
На всю очередь работала только одна касса, поэтому продажа билетов шла очень медленно, приводя «постояльцев» очереди
в отчаяние. Самые сообразительные быстро заметили, что, как правило, несколько билетов в одни руки кассир продаёт
 быстрее, чем когда эти же билеты продаются по одному. Поэтому они предложили нескольким подряд стоящим людям
 отдавать деньги первому из них, чтобы он купил билеты на всех.

Однако для борьбы со спекулянтами кассир продавала не более 3-х билетов в одни руки, поэтому договориться
таким образом между собой могли лишь 2 или 3 подряд стоящих человека.

Известно, что на продажу i-му человеку из очереди одного билета кассир тратит Ai секунд, на продажу двух
билетов — Bi секунд, трех билетов — Ci секунд. Напишите программу, которая подсчитает минимальное время,
за которое могли быть обслужены все покупатели.

Обратите внимание, что билеты на группу объединившихся людей всегда покупает первый из них. Также никто в
целях ускорения не покупает лишних билетов (то есть билетов, которые никому не нужны).

Формат ввода
На вход программы поступает сначала число N — количество покупателей в очереди (1 ≤ N ≤ 5000). Далее идет N
троек натуральных чисел Ai, Bi, Ci. Каждое из этих чисел не превышает 3600. Люди в очереди нумеруются, начиная от кассы.

"""

"""
задача на оптимизацию
"""

n = int(input())

m = 10**9
l = [[m, m, m], [m, m, m], [m, m, m]]
for _ in range(n):
    l.append([int(i) for i in input().split()])

dp = [0, 0, 0]
for i in range(3, 3+n):
    dp.append(min([dp[i-1] + l[i][0], dp[i-2] + l[i-1][1], dp[i-3] + l[i-2][2]]))

print(dp[-1])

'''
t = 0
if len(l) == 0:
    print(0)
    exit(0)

elif len(l) == 1:
    print(min(l[0][0] + l[1][0], l[0][1]))
    exit(0)

elif len(l) == 2:
    print(min(l[0][0] + l[1][0], l[0][1]))
    exit(0)

for i in range(3, len(l), 3):
    pass
'''



