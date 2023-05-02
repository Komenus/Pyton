# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

N = int(input('Введите длину массива: '))
nums = []
for i in range(N):
    num = random.randint(1, 30)
    nums.append(num)
print(nums) 

Nmin = int(input('Введите минимальное значение: '))
Nmax = int(input('Введите максимальное значение: '))

for i in range(len(nums)):
    if Nmin < nums[i] < Nmax:
        print(i)