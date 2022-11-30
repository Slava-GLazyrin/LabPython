from pyDatalog import pyDatalog

"""
Задание 2 - Вычислить среднее значение ряда
"""

pyDatalog.create_terms('Kol, averageValue')

averageValue[Kol] = (Kol+1)/2

print(Kol == averageValue[100])
