# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Простые делители числа
# in
# 54
# out
# [2, 3, 3, 3]
# in
# 9990
# out
# [2, 3, 3, 3, 5, 37]
# in
# 650
# out
# [2, 5, 5, 13]

def find_the_divisors_of_a_number(n):
   i = 2
   list = []
   while i * i <= n:
       while n % i == 0:
           list.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       list.append(n)
   return list
print(find_the_divisors_of_a_number(9990))
