import pygame
import random
import subprocess
import sys
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
x1 = 0
y1 = 0
food = random.randint(0,3)
game_close = False
font_style = pygame.font.SysFont("bahnschrift", 25)
game_over = 0
x_circle = 50
y_circle = 400
score = 0
score = round(score,1)
clocked = 0
# радиус круга
r = 40

# цвет круга
red = (255, 0, 0)
neutral = (125,125,125)
neutralen = (125,125,125)
neutralne = (125,125,125)
boom = (250, 100, 5)
green = (0,255,0)
ne = (125,125,125)
en = (125,125,125)
blue = (0, 0, 255)
def message1(msg, color):
      mesg = font_style.render(msg, True, color)
      screen.blit(mesg, [100,400])  
def message(msg, color):
      mesg = font_style.render(msg, True, color)
      screen.blit(mesg, [100,300])
def draw_score(screen, score):
   score_surface = font_style.render(f"Очки: {score}", True, (255, 255, 255))
   screen.blit(score_surface, (400, 10))
   clock_surface = font_style.render(f"Время: {clocked}", True, (255, 255, 255))
   screen.blit(clock_surface, (200, 10))
while game_close != True:
    while game_over == 1:
           screen.fill(neutral)
           message("Вы проиграли! Нажмите Q для выхода", red)
           message1("Или R для рестарта", red)
           draw_score(screen, score)
           pygame.display.update()
           for event in pygame.event.get():
              if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_q:
                         pygame.quit()
                         subprocess.run(["python", "Menu.py"])
                         sys.exit()
                   if event.key == pygame.K_r:
                        pygame.quit()
                        subprocess.run(["python", "Курсовая1.py"])
                        sys.exit()
                      
    clocked +=0.1
    clocked = round(clocked,1)
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
    if keys[pygame.K_UP]:
        y = y - 50
    if keys[pygame.K_DOWN]:
        y = y + 50
        #реакция
    if food == 0:
        x1 = 100
        y1 = 350
        ne = green
        pygame.display.update()
        if x == 700 or y == HEIGHT//2+200 or y == HEIGHT//2 -200:
            game_over = 1
        elif x ==100:
           x = 400
           y = 400
           ne = (125,125,125)
           en = (125,125,125)
           food = random.randint(0,3)
           screen.fill((boom))
           pygame.draw.circle(screen, red, (x, y), r)
           clocked = round(clocked, 1)
           score += 1/clocked
           score = round(score, 1)
           clocked = 0
           pygame.display.update()
           pygame.time.delay(120)
    if food ==2:
        x1 = 350
        y1 = 100
        ne = green
        pygame.display.update()
        if y == 700 or x == WIDTH//2 +200 or x == WIDTH//2-200:
            game_over =1
        elif y ==100:
            x = 400
            y = 400
            ne = (125,125,125)
            en = (125,125,125)
            food = random.randint(0,3)
            screen.fill((boom))
            pygame.draw.circle(screen, red, (x, y), r)
            clocked = round(clocked, 1)
            score += 1/clocked
            score = round(score, 1)
            clocked = 0
            pygame.display.update()
            pygame.time.delay(120)
    if food == 3:
        x1 = 350
        y1 = 600
        ne = green
        pygame.display.update()
        if y == 100 or x == WIDTH//2 +200 or x == WIDTH//2-200:
            game_over = 1
        elif y == 600:
            x = 400
            y = 400
            ne = (125,125,125)
            en = (125,125,125)
            food = random.randint(0,3)
            screen.fill((boom))
            pygame.draw.circle(screen, red, (x, y), r)
            clocked = round(clocked, 1)
            score += 1/clocked
            score = round(score, 1)
            clocked = 0
            pygame.display.update()
            pygame.time.delay(120)
            
             
        
            
         
         
    if food ==1:
        x1 = 680
        y1 = 350
        ne = green
        pygame.display.update()
        if x == 100 or y == HEIGHT//2 +200 or y == HEIGHT//2 -200:
            game_over = 1
        elif x ==700:
           x = 400
           y = 400
           ne = (125,125,125)
           en = (125,125,125)
           food = random.randint(0,3)
           screen.fill((boom))
           pygame.draw.circle(screen, red, (x, y), r)
           clocked = round(clocked, 1)
           score += 1/clocked
           score = round(score, 1)
           clocked = 0
           pygame.display.update()
           pygame.time.delay(120)
        
    
           
    screen.fill((neutral))
    pygame.draw.rect(screen, ne, [x1,y1, 90,100])
    pygame.draw.circle(screen, red, (x,y), r)
    draw_score(screen, score)
    pygame.display.update()
    pygame.time.delay(30)
