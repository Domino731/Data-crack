import random

import pygame

data_wall_width = 50
data_wall_height = 140
space_between_columns = 35
window_width = 800
max_bottom = 500
max_top = 40


def create_random_wall_x():
    return random.randint(max_top, max_bottom)


class DataWall():
    def __init__(self, x, y):
        self.is_cracked = False
        self.velocity = 3
        self.x = x
        self.y1 = y
        self.y2 = y + data_wall_height + space_between_columns
        self.top_y2 = self.y1 + data_wall_height
        self.bot_y1 = self.y1 + data_wall_height + space_between_columns

    def draw(self, screen):
        pygame.draw.rect(screen, "white", pygame.Rect(self.x, self.y1, data_wall_width, data_wall_height))
        pygame.draw.rect(screen, "white",
                         pygame.Rect(self.x, self.y2 + space_between_columns, data_wall_width, data_wall_height))

    def update(self):
        if self.is_cracked: return

        # Check if the top edge has reached the screen boundary
        if self.y1 <= max_top:
            self.velocity = abs(self.velocity)  # Reverse the velocity to bounce down

        # Check if the bottom edge has reached the screen boundary
        if self.y2 >= max_bottom:
            self.velocity = -abs(self.velocity)  # Reverse the velocity to bounce up

        self.y1 += self.velocity
        self.y2 += self.velocity
        self.top_y2 += self.velocity
        self.bot_y1 += self.velocity
