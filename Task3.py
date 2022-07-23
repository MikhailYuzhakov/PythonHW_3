# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.

import random
maxNumb = 0
minNumb = 1

list = [round(random.uniform(1.0, 101.0), 3) for i in range(1, 11)] # генерируем список из 10 элементов, состоящий из случайных чисел от 1 до 101...
print("Исходный массив дробных чисел:")
print(list)

fractPart = [round(list[i]%1, 3) for i in range(len(list))]
print("Массив дробных частей чисел")
print(fractPart)

for item in fractPart:
    if (item > maxNumb): maxNumb = item
    if (item < minNumb): minNumb = item
print("Максимальная и минимальная дробные части: ", maxNumb, minNumb)
print("Разность минимальной и максимальной дробных частей = ", maxNumb - minNumb)
