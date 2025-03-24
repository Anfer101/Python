import pygame

pygame.init()

# укажем размер окна
WIDTH = 800
HEIGHT = 600

# создадим окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# координаты круга
x = 50
y = 50

# Создадим переменные для изменеия скорости координат
speed_x = 1
speed_y = 1

# радиус круга
r = 40

# цвет круга
red = (255, 0, 0)
red_1 = 2
red_change = 0
changeg = 255
changeb= 255

# цвет фона
blue = (0, 0, 255)

#Загружаем картинку

sprite_sheet = pygame.image.load("1.png")

#Создаем список и закидываем в него картинки
# Добавляем модуль pygame.SRCALPHA

"""
pygame.Surface - поверхности в Pygame используются
для представления внешнего вида объекта и его положения на экране. 
"""

"""
pygame.SRCALPHA — это флаг, который указывает на то,
что поверхность имеет альфа-канал для прозрачности
"""

sprites = []
for i in range(sprite_sheet.get_width()//12):
    surface = pygame.Surface((50, 50), pygame.SRCALPHA)
    rect = pygame.Rect(i *80 + 15 , 15 , 60, 60)
    surface.blit(sprite_sheet, (0, 0), rect)
    sprites.append(surface)


sprites_1 = []
for i in range(7):
    surface = pygame.Surface((80, 50), pygame.SRCALPHA)
    rect = pygame.Rect(i *80 + 5 , 95 , 100, 60)
    surface.blit(sprite_sheet, (0, 0), rect)
    sprites_1.append(surface)

# Создаем переменную для анамирования картинки
animation_count = 0
animation_count_1 = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    x += speed_x
    y += speed_y

    # Допишем программу, чтобы шарик не уходил за рамки экрана
    if x > WIDTH - r or x < r:
        speed_x = speed_x * -1
    if y > HEIGHT - r or y < r:
        speed_y = speed_y * -1
 
    # Зарисовываем круги синим цветом
    screen.fill((red_1, changeg, changeb))

    # Работаем с анимацией
    animation_count += 1
    animation_count = animation_count % 11
    animation_count_1 += 1
    animation_count_1 = animation_count % 7

    
    if red_1 != 255:
        red_change =1
        red_1 = red_1+red_change
        changeg = changeg-1
        changeb=changeb-1
    if red_1 == 255:
        red = (255, 0, 0)
        red_1 = 2
        red_change = 0
        changeg = 255
        changeb= 255
        screen.fill((red_1, changeg, changeb))
       

    # Рисуем картинку по середине
    screen.blit(sprites[animation_count], (x, HEIGHT / 2))
    screen.blit(sprites_1[animation_count_1], (x, 100))
    # нарисуем круг
    #pygame.draw.circle(screen, red, (x, y), r)
    
    pygame.display.update()
    pygame.time.delay(30)
