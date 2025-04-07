a = int(input("кол-во шариков"))

while a > 10:
    a = int(input("кол-во шариков(до 10)"))


col_1 , col_2 = 0, 0
sum_1 , sum_2 = 0, 0

for i in range(a):
            x = int(input())
            while x >100:
                x = int(input("введите заново число(до 100)"))
            if x % 2 == 0:
                col_1 += 1
                sum_1 +=x
            if x % 2 != 0:
                col_2 +=1
                sum_2 +=x
                
print("Кол-во нечётных чисел =", col_2, ", а их сумма =",sum_2)
print("Кол-во чётных чисел =", col_1, ", а их сумма =",sum_1)
            




