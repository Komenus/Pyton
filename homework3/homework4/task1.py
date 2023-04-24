# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

import random
N1 = int(input('Введите длину первого набора чисел: '))
N2 = int(input('Введите длину второго набора чисел: '))
nums1 = []
nums2 = []
for i in range(N1):
    num = random.randint(1, 10)
    nums1.append(num)
for i in range(N2):
    num = random.randint(1, 10)
    nums2.append(num) 
set_1 = set(nums1)  
print(set_1)
set_2 = set(nums2) 
print(set_2)
set_r = set_1 & set_2
print(set_r)
my_list = list(set_r)
my_list.sort()
print(my_list)

