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
game_over = 0
x_circle = 50
y_circle = 400
score = 3
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
   screen.blit(mesg, [100,300])
def message1(msg,color):
   mesg = font_style.render(msg, True, color)
   screen.blit(mesg, [100,400])
def draw_score(screen, score):
   score_surface = font_style.render(f"Призы: {score}", True, (255, 255, 255))
   screen.blit(score_surface, (10, 10))
while game_close != True:
    while game_over == 1:
           screen.fill(neutral)
           message("Вы проиграли! Нажмите Q для выхода", red)
           message1("или C для повторной игры", red)
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
        if x == 700:
            game_over = 1
        elif x ==100:
           x = 400
           y = 400
           ne = (125,125,125)
           en = (125,125,125)
           food = random.randint(0,1)
           screen.fill((boom))
           pygame.draw.circle(screen, red, (x, y), r)
           pygame.display.update()
           pygame.time.delay(65)
         
         
    if food ==1:
        en = green
        pygame.display.update()
        if x == 100:
            game_over = 1
        elif x ==700:
           x = 400
           y = 400
           ne = (125,125,125)
           en = (125,125,125)
           food = random.randint(0,1)
           screen.fill((boom))
           pygame.draw.circle(screen, red, (x, y), r)
           pygame.display.update()
           pygame.time.delay(65)
         
    screen.fill((neutral))
    pygame.draw.rect(screen, ne, [50,350, 90,100])
    pygame.draw.rect(screen, en, [660,350, 90,100])
    pygame.draw.circle(screen, red, (x,y), r)
    pygame.display.update()
    pygame.time.delay(30)
