import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("столкновение")
clock = pygame.time.Clock()
running = True

player_color = (0, 128, 255)
player_size = 50
player_x = 100
player_y = 525
player_speed = 1

sprites = [pygame.Rect(10, 540, 580, 50),
           pygame.Rect(590, 280, 50, 350),
           pygame.Rect(10, 390, 400, 50),
           pygame.Rect(10, 130, 680, 50)]

cx, cy, cz = 255, 255, 255

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    q1 = pygame.Rect(player_x, player_y, player_size, player_size) #управляемый квадрат 
    rect1 = pygame.Rect(100, 200, 50, 50) #белый
    rect2 = pygame.Rect(100, 450, 50, 50) #красный
    lab1 = pygame.Rect(590, 280, 50, 350)
    lab2 = pygame.Rect(10, 540, 580, 50),
    lab3 = pygame.Rect(590, 280, 50, 350),
    lab4 = pygame.Rect(10, 390, 400, 50),
    lab5 = pygame.Rect(10, 130, 680, 50)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed



    if q1.colliderect(rect1):
        screen.fill((0, 0, 0))
        cx, cy, cz = 0, 0, 0
        pygame.draw.rect(screen, player_color, q1)
        pygame.draw.rect(screen, (255, 100, 100), rect2)
        pygame.display.flip()
    else:
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, player_color, q1)
        pygame.draw.rect(screen, (cx, cy, cy), rect1)
        pygame.draw.rect(screen, (255, 100, 100), rect2)
        pygame.display.flip()

    if q1.colliderect(rect2):
        screen.fill((0, 0, 0))
        cx, cy, cz = 255, 255, 255
        pygame.draw.rect(screen, player_color, q1)
        pygame.draw.rect(screen, (cx, cy, cy), rect1)
        pygame.draw.rect(screen, (255, 100, 100), rect2)
        pygame.display.flip()
        if running == True:
            for sprite in sprites:
                pygame.draw.rect(screen, (255, 0, 0), sprite)
                pygame.display.flip()
        pygame.display.flip()
    
    clock.tick(90)

pygame.quit()
