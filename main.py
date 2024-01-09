# Example file showing a circle moving on screen
import math

import pygame

from data_wall import DataWall

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
width, height = pygame.display.get_surface().get_size()

container_padding = 30
container_offset = math.floor(container_padding / 2)
container_width = width - container_padding
container_height = height - container_padding
def draw_container():
    pygame.draw.rect(screen, "red", pygame.Rect(container_offset, container_offset,container_width, container_height), 2)


def draw_bridge():
    pygame.draw.rect(screen, "red", pygame.Rect(container_offset, (height / 2) - 15, container_width, 30))


data_walls = []

data_walls.append(DataWall(40, 40))

def draw_data_walls():
    for wall in data_walls:
        wall.draw(screen)

print(width, height)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    pygame.draw.circle(screen, "yellow", player_pos, 40)
    draw_container()
    draw_bridge()
    draw_data_walls()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()