import pygame
import subprocess
import sys

# Настройки меню
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Меню игры")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
RED = (255, 0, 0)

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
    subprocess.run(["python", "Курсовая.py"])  # Запускаем игру
    sys.exit()     # Закрываем всё после игры

def main_menu():
    while True:
        screen.fill(BLACK)
        
        # Заголовок
        title = font.render("Игра на Реакцию", True, WHITE)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 100))
        
        # Кнопки
        draw_button("Старт", WIDTH//2 - 100, HEIGHT//2 - 30, start_game)
        draw_button("Выход", WIDTH//2 - 100, HEIGHT//2 + 50, sys.exit)
        
        # Выход по крестику
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()

if __name__ == "__main__":
    main_menu()
