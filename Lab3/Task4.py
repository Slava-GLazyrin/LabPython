from pyDatalog import pyDatalog
import random

"""
Задание 4 - Вычислить медиану 100 случайных чисел в диапазоне от 1 до 100
"""


pyDatalog.create_terms('Kol, median')

median[Kol] = (random.randint(1,100) + median[Kol-1]) / 2
median[0] = 1


print(Kol == median[100])
