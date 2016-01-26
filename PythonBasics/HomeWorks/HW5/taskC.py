# -*- coding: utf-8 -*
# Во входной строке записана последовательность чисел через пробел.
# Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось в последовательности или NO, если не встречалось.

# Входные данные
# Вводится список чисел. Все числа списка находятся на одной строке.

# Выходные данные
# Выведите ответ на задачу.

input_numbers = map(int, input().split())
set_numbers = set()
for number in input_numbers:
    if number in set_numbers:
        print("YES")
    else:
        print("NO")
        set_numbers.add(number)

