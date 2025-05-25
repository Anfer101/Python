import pygame
import subprocess
import sys

# Настройки меню
pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Меню игры")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
x = 50
y = 400
x_speed = 5
y_speed = 5
Riru = -1
# Шрифты
font = pygame.font.SysFont('Arial', 50)

def draw_button(text, x, y, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    # Рисуем кнопку
    button_rect = pygame.Rect(x, y, 200, 50)
    color = RED if button_rect.collidepoint(mouse) else GRAY
    pygame.draw.rect(screen, color, button_rect, border_radius=10)
    
    # Текст кнопки
    text_surf = font.render(text, True, WHITE)
    text_rect = text_surf.get_rect(center=button_rect.center)
    screen.blit(text_surf, text_rect)
    
    # Обработка клика
    if click[0] == 1 and button_rect.collidepoint(mouse) and action:
        action()

def start_game():
    pygame.quit()  # Закрываем меню
    subprocess.run(["python", "Курсовая2.py"])  # Запускаем игру
    sys.exit()     # Закрываем всё после игры
def exit2():
    pygame.quit()
    sys.exit()
def main_menu(x, x_speed, y, y_speed):
    while True:
        screen.fill(BLACK)
        # Заголовок
        title = font.render("Игра на Реакцию", True, WHITE)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 100))
        
        # Кнопки
        draw_button("Старт", WIDTH//2 - 100, HEIGHT//2 - 30, start_game)
        draw_button("Выход", WIDTH//2 - 100, HEIGHT//2 + 50, exit2)
            
        # Выход по крестику
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        x+=x_speed
        y+=y_speed
        if x > 785:
            x_speed *=Riru
            y_speed +=1
        if x < 15:
            x_speed*=Riru
            y_speed -=1
        if y > 785:
            y_speed*=Riru
        if y<15:
            y_speed*=Riru
        if x_speed <0:       
            pygame.draw.circle(screen, BLUE, (x,y), 40)
        if x_speed >0:
            pygame.draw.circle(screen, GREEN, (x,y), 40)
        if x_speed <0 and y_speed < 0:
            pygame.draw.circle(screen, YELLOW, (x,y), 40)
        if x_speed > 0 and y_speed >0:
            pygame.draw.circle(screen, RED, (x,y), 40)
        
            
        pygame.display.update()
        pygame.time.delay(25)

if __name__ == "__main__":
    main_menu(x,x_speed, y,y_speed)
