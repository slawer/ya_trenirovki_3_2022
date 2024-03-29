

"""
https://contest.yandex.ru/contest/45468/problems/22

22. Кузнечик
Ограничение времени	1 секунда
Ограничение памяти	64Mb
Ввод	стандартный ввод или input.txt
Вывод	стандартный вывод или output.txt
У одного из студентов в комнате живёт кузнечик, который очень любит прыгать по клетчатой одномерной доске.
Длина доски — N клеток. К его сожалению, он умеет прыгать только на 1, 2, …, k клеток вперёд.

Однажды студентам стало интересно, сколькими способами кузнечик может допрыгать из первой клетки до последней.
Помогите им ответить на этот вопрос.

Формат ввода
В первой и единственной строке входного файла записано два целых числа — N и k .

Формат вывода
Выведите одно число — количество способов, которыми кузнечик может допрыгать из первой клетки до последней.
"""


def kuz(n, k):
    if n == 1:
        return 1

    elif n == 2:
        return 1

    elif n == 3:
        return 1 if k == 1 else 2

    dp = [0 for _ in range(n + 1)]
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1  # в тесте 3 = 10 10 падает с 1
    dp[3] = 2 if k > 1 else 1

    for i in range(4, n + 1):
        s = 0
        for j in range(i - 1, max(0, i - 1 - k), -1):
            s += dp[j]
        dp[i] = s

    print(dp)
    return dp[n]


#n, k = [int(e) for e in input().split()]
#a = kuz(n, k)
#print(a)

#  тест
test = {
    (8, 2): 21,
    (1, 10): 1,
    (10, 10): 256,
    # (30, 1):
}

for (n, k), a in test.items():
    print('\ntest', n, k)
    r = kuz(n, k)
    if a != r:
        print('!!!error:')
