# Example file showing a circle moving on screen
import math

import pygame

from data_wall import DataWall, create_random_wall_x

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
    pygame.draw.rect(screen, "red", pygame.Rect(container_offset, container_offset, container_width, container_height),
                     2)


bridge_offset_y = (height / 2) - 15
bridge_height = 30


def draw_bridge():
    pygame.draw.rect(screen, "red", pygame.Rect(container_offset, bridge_offset_y, container_width, bridge_height))


data_walls = []

walls_padding = 40
space_for_walls = width - 2 * 40
walls_amount = 2
space_between_walls = 40
start_x = 40
for i in range(walls_amount):
    data_walls.append(DataWall(start_x, create_random_wall_x()))
    start_x += 40 + space_between_walls


def draw_data_walls():
    for wall in data_walls:
        wall.draw(screen)


def update_data_walls():
    for wall in data_walls:
        wall.update()


current_wall_index = 0
current_wall = data_walls[current_wall_index]


def check_if_data_crack():
    y1 = current_wall.top_y2
    y2 = current_wall.bot_y1
    bridge_y1 = bridge_offset_y - 10
    bridge_y2 = bridge_offset_y + bridge_height + 10
    bridge_range = range(int(bridge_y1), int(bridge_y2))
    print(y1, y2)
    print("range: ", bridge_range)
    if y1 < bridge_y1 and bridge_y2 > y2:
        current_wall.is_cracked = True
        current_wall_index = 1

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                check_if_data_crack()
    keys = pygame.key.get_pressed()

    # Check if the spacebar is pressed
    # if keys[pygame.K_SPACE]:
    #     check_if_data_crack()

    update_data_walls()
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
