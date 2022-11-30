from pyDatalog import pyDatalog


"""
Задание 1
Посчитать сумму ряда
"""


pyDatalog.create_terms('Kol, summa')

summa[Kol] = Kol + summa[Kol-1]
summa[1] = 1

print(Kol == summa[100])
