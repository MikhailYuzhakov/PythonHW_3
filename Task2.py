# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint
mltpx = [] # переменная для хранения результата перемножения пар чисел

list = [randint(1, 101) for i in range(1, 11)] # генерируем список из 10 элементов, состоящий из случайных чисел от 1 до 101...
print(list)

N = len(list)
for i in range(N):
    mltpx.append(list[i] * list[N-1]) # переменожаем пары чисел
print(mltpx)