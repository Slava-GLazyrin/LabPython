from pyDatalog import pyDatalog
import random

"""
Задание 3 - Вычислить произведение 100 случайных чисел в диапазоне от 1 до 100
"""


pyDatalog.create_terms('Kol, productRandomNumbers')

productRandomNumbers[Kol] = random.randint(1,100) * productRandomNumbers[Kol-1]
productRandomNumbers[0] = 1

print(Kol == productRandomNumbers[100])
