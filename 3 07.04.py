a =int(input("Кол-во чисел "))
n, b = 0, 0
while a > 20:
    a =int(input("Кол-во чисел( до 20!) "))

for i in range(a):
    x =int(input("число "))
    if x % 3 == 0 and x % 2 !=0:
           n +=1
    if x %3 == 0 and x%2 == 0:
           b +=1
print("числа, которые делятся на 3 -", n)
print("числа, которые делятся на 6 -", b)
    
