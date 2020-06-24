"""
6. Реализовать два небольших скрипта:
    а) итератор, генерирующий целые числа, начиная с указанного,
    б) итератор, повторяющий элементы некоторого списка, определенного заранее.
    Подсказка: использовать функцию count() и cycle() модуля itertools.
    Обратите внимание, что создаваемый цикл не должен быть бесконечным.
    Необходимо предусмотреть условие его завершения.
    Например, в первом задании выводим целые числа, начиная с 3,
    а при достижении числа 10 завершаем цикл. Во втором также необходимо
    предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""

from itertools import count, takewhile

USR_INT_MIN, USR_INT_MAX = int(input("Введите начальное целое число: ")), \
                           int(input("Введите конечное целое число: "))

# Использую генераторы, т.к. работают быстрее
RESULT = [ELEM for ELEM in takewhile(lambda x: x <= USR_INT_MAX, count(USR_INT_MIN))]
print(f"Список целых чисел от {USR_INT_MIN} до {USR_INT_MAX} - {RESULT}")

"""
Введите начальное целое число: 3
Введите конечное целое число: 10
Список целых чисел от 3 до 10 - [3, 4, 5, 6, 7, 8, 9, 10]
"""
