# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

n = int(input('Введите трехзачное число: '))
if  99 < n < 100000:
    # n1 = n // 100
    # n2 = (n - n1* 100) // 10 #убираем сотни
    # n3 = (n - n1* 100) % 10  #берем остаток от деления двухзначного
    # sumn = n1 + n2 + n3
    temp = 0
    while n > 0:
        n1 = n  % 10
        temp += n1
        n = n // 10 
    print(temp)
  

else:
     print ('Вы ввели не трехзначное число: ')



# temp = 0
# while n > 0:
#     n1 = n  % 10
#     temp += n1
#     n = n // 10 
# print(temp)
