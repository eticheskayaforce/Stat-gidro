# вычисление статистических характеристик
from VigruzkaTXT2 import read_data
from statistics import mean #из модуля статистика импортируем функцию среднего
from statistics import variance #дисперсия
from statistics import stdev #ср.квадратическое отклонение

Q = read_data()
Qsr = mean(Q) #задаем параметр среднего
DQ = variance(Q)
STQ = stdev(Q)


print(Qsr)
print(DQ)
print(STQ)


