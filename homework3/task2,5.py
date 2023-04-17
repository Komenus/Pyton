# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

import random
N = int(input('Введите длину массива: '))
X = int(input('Введите число X: '))
res = 0
res2 = 0
nums = []
for i in range(N):
    num = random.randint(1, 10)
    # num = int(input())  #для ручной проверки программы
    nums.append(num)
dif =abs(X - nums[0] ) 
print(nums)  
for i in range(1,N):
        if  dif > abs(X - nums[i]):
            dif = abs(X - nums[i]) 
            res = nums[i] 
        elif dif == X - nums[0]:
            res = nums[0] 
        elif abs(nums[i] - X) == dif:
            res2 = nums[i]       
                          
print(f'наиболее близкое число: {res}')  
if res2 != 0 and res2 !=res:
    print(f'Второе наиболее близкое число: {res2}')         