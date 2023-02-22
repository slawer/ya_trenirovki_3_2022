

"""
https://contest.yandex.ru/contest/45468/problems/
Вовочка ломает систему безопасности Пентагона. Для этого ему понадобилось узнать,
какие символы в секретных зашифрованных посланиях употребляются чаще других. Для удобства изучения
Вовочка хочет получить графическое представление встречаемости символов. Поэтому он хочет построить гистограмму
количества символов в сообщении. Гистограмма — это график, в котором каждому символу, встречающемуся в сообщении
хотя бы один раз, соответствует столбик, высота которого пропорциональна количеству этих символов в сообщении.


"""

"""
разобрана в тренировках по теме словари

но ввод большой и заранее неизвестно сколько строк


"""

vv = '''Twas brillig, and the slithy toves
Did gyre and gimble in the wabe;
All mimsy were the borogoves,
And the mome raths outgrabe.'''

from collections import defaultdict

# vv = input()
with open('input.txt', 'r') as f:
    vv = f.read()

m = 0
d = defaultdict(int)
for w in vv.split():
    for s in w.strip():
        d[ord(s)] += 1
        m = max(m, d[ord(s)])


for i in range(1, m+1):
    l = []
    for s in sorted(d):
        l.append('#' if d[s] > m - i else ' ')

    print(''.join(l))


print(''.join(map(chr, sorted(d))))



