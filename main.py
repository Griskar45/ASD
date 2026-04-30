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
class Maze:
    def __init__(self, cols, rows, cell_size):   # ← вот эти параметры
        self.cols = cols
        self.rows = rows
        self.cell_size = cell_size
    def draw(self,surface):
        for y in range(self.rows):
            for x in range(self.cols):
                rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(surface, (100,100,100), rect,1)
maze = Maze(20,15,30)
while running:
    # Обработка выхода
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Заливаем фон чёрным
    screen.fill((0, 0, 0))
    maze.draw(screen)
    # Обновляем экран
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()