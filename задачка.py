a, b, c = 0, 0, 0
n = 0
avto = 0
while n == 0:
    x = int(input("Скорость авто"))
    while x ==0:
        x = int(input("невозможная скорость авто"))
    if x < 60 and x > 10:
            a +=1
            avto = avto+1
    if x > 60 and x < 90:
            b +=1
            avto = avto+1
    if x > 90:
            c +=1
            avto = avto+1
    if x < 10:
            n=1
            print(a, "- безопасная скорость,", b, "- средняя скорость,", c, "- высокая скорость, а",avto, "- общее кол-во авто")
