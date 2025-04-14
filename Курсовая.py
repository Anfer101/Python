import pygame
import random

pygame.init()

# укажем размер окна
WIDTH = 800
HEIGHT = 800

# создадим окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# координаты круга
x = 400
y = 400

# Создадим переменные
food = random.randint(0,1)
game_close = False
font_style = pygame.font.SysFont("bahnschrift", 25)
# радиус круга
r = 40

# цвет круга
red = (255, 0, 0)
neutral = (125,125,125)
boom = (250, 100, 5)
green = (0,255,0)
ne = (125,125,125)
en = (125,125,125)
blue = (0, 0, 255)

def message(msg, color):
   mesg = font_style.render(msg, True, color)
   screen.blit(mesg, [400,400])

while game_close != True:
    while game_close == True:
           screen.fill(blue)
           message("Вы проиграли! Нажмите Q для выхода или C для повторной игры", red)
           pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #движение
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x = x-50
    if keys[pygame.K_RIGHT]:
        x = x+50
        #реакция
    if food == 0:
        ne = green
        pygame.display.update()
    if food ==1:
        en = green
        pygame.display.update()    
    if x ==100:
        x = 400
        y = 400
        ne = (125,125,125)
        en = (125,125,125)
        food = random.randint(0,1)
        screen.fill((boom))
        pygame.draw.circle(screen, red, (x, y), r)
        pygame.display.update()
        pygame.time.delay(65)
    if x == 700:
        game_close = True
    screen.fill((neutral))
    pygame.draw.rect(screen, ne, [50,350, 90,100])
    pygame.draw.rect(screen, en, [660,350, 90,100])
    pygame.draw.circle(screen, red, (x,y), r)
    pygame.display.update()
    pygame.time.delay(30)
