import pygame

data_wall_width = 30
data_wall_height = 30
space_between_columns = 40


class DataWall():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.rect(screen, "white", pygame.Rect(self.x, self.y, data_wall_width, data_wall_height))
        pygame.draw.rect(screen, "white", pygame.Rect(self.x, self.y + space_between_columns, data_wall_width, data_wall_height))
