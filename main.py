import pygame
import sys

# Размеры окна
WIDTH = 800
HEIGHT = 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze")
clock = pygame.time.Clock()

running = True
while running:
    # Обработка выхода
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заливаем фон чёрным
    screen.fill((0, 0, 0))

    # Обновляем экран
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()