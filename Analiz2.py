# вычисление статистических характеристик
from VigruzkaTXT2 import (Q)
print(Q)
from statistics import mean #из модуля статистика импортируем функцию среднего
Qsr = mean(Q) #задаем параметр среднего
for line in Q #читаем значения Q  по строкам
    line = line.strip(" \n")  # отбрасываем начальные и конечные пробелы

