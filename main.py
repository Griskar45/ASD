import pygame
import random

COLOR_WALL = (40, 40, 40)
COLOR_PATH = (230, 230, 230)
COLOR_START = (100, 255, 100)
COLOR_END = (255, 100, 100)

class Maze:
    def __init__(self, cols, rows, cell_size):
        self.cols = cols
        self.rows = rows
        self.cell_size = cell_size
        # Инициализируй всю сетку стенами (1)
        self.grid = [[1] * cols for _ in range(rows)]
        # Задай старт и финиш (пока можно вручную)
        self.start = (1, 1)
        self.end = (cols - 2, rows - 2)

    def draw(self, surface):
        # закрась клетки: для стены один цвет, для прохода — другой
        # особо отметь старт и финиш
        pass