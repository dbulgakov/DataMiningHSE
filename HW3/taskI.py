# -*- coding: utf-8 -*
# Даны числа a, b, c, d.
# Выведите в порядке возрастания все целые числа от 0 до 1000, которые являются корнями уравнения ax^3+bx^2+cx+d=0.

# Входные данные
# Вводятся целые числа a, b, c и d.

# Выходные данные
# Выведите ответ на задачу. Если в указанном промежутке нет корней уравнения, то ничего выводить не нужно.

a = int(input())
b = int(input())
c = int(input())
d = int(input())

for i in range (0, 1001):
    if (a * i ** 3 + b * i** 2 + c * i + d == 0):
        print(i)

