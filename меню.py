import pygame
import random

pygame.init()


# укажем размер окна
WIDTH = 800
HEIGHT = 800

# создадим окно
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# координаты круга
game_close = False
font_style = pygame.font.SysFont("bahnschrift", 25)
game_over = 0
x = 50
y = 400
score = 3
speed_x = 10
speed_y = 10
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
while game_close != True:
    while game_over == 1:
           screen.fill(neutral)
           pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    message("Игра", red)
    def run(x, speed_x, speed_y, y, HEIGHT, WIDTH, neutral, red, r, screen):
        screen.fill((neutral))
        pygame.draw.circle(screen, red, (x,y), r)
        pygame.display.update()
        pygame.time.delay(30)
    run(x, speed_x, speed_y, y, HEIGHT, WIDTH, neutral, red, r, screen)
    x += speed_x
    y += speed_y
    if x > WIDTH - r or x < r:
        speed_x = speed_x * -1
    if y > HEIGHT - r or y < r:
        speed_y = speed_y * -1
