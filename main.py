import math
import pygame
from data_wall import DataWall, create_random_wall_x

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
CONTAINER_PADDING = 30
BRIDGE_HEIGHT = 30
WALLS_AMOUNT = 15
SPACE_BETWEEN_WALLS = 40
START_X = 40

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

# Images
img_game_over = pygame.image.load("C:\\Users\\Dominik\\Desktop\\projects\\Data-crack\\game-over.png").convert()
img_game_over = pygame.transform.scale(img_game_over, (SCREEN_WIDTH, SCREEN_HEIGHT))
img_background = pygame.image.load("C:\\Users\\Dominik\\Desktop\\projects\\Data-crack\\background.png").convert()
img_background = pygame.transform.scale(img_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
# Player setup
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# Container setup
container_offset = math.floor(CONTAINER_PADDING / 2)
container_width = SCREEN_WIDTH - CONTAINER_PADDING
container_height = SCREEN_HEIGHT - CONTAINER_PADDING

# Bridge setup
bridge_offset_y = (SCREEN_HEIGHT / 2) - 15
bridge_y1, bridge_y2 = bridge_offset_y - 5, bridge_offset_y + BRIDGE_HEIGHT + 5
bridge_range = range(int(bridge_y1), int(bridge_y2))

def draw_container():
    pygame.draw.rect(
        screen, "red",
        pygame.Rect(container_offset, container_offset, container_width, container_height),
        2
    )


def draw_bridge():
    pygame.draw.rect(
        screen, "red",
        pygame.Rect(container_offset, bridge_offset_y, container_width, BRIDGE_HEIGHT)
    )
    pygame.draw.rect(screen, "yellow",
                     pygame.Rect(container_offset, bridge_y1, container_width, 1))
    pygame.draw.rect(screen, "yellow",
                     pygame.Rect(container_offset, bridge_y2, container_width, 1))

def create_data_walls():
    data_walls = []
    x_position = START_X
    for _ in range(WALLS_AMOUNT):
        data_walls.append(DataWall(x_position, create_random_wall_x()))
        x_position += SPACE_BETWEEN_WALLS + START_X
    return data_walls


class Game:
    def __init__(self):
        self.current_wall_index = 0
        self.data_walls = create_data_walls()
        self.current_wall = self.data_walls[self.current_wall_index]
        self.is_game_over = False
    def draw_walls(self):
        for wall in self.data_walls:
            wall.draw(screen)

    def draw_game_over(self):
        if self.is_game_over:
            screen.blit(img_game_over, (0, 0))

    def update(self):
        for wall in self.data_walls:
            wall.update()

    def reset_walls(self):
        self.current_wall_index = 0
        self.current_wall = self.data_walls[self.current_wall_index]
        for wall in self.data_walls:
            wall.is_cracked = False

    def check_if_data_crack(self):
        y1, y2 = self.current_wall.top_y2, self.current_wall.bot_y1
        wall_range = range(y1, y2)

        if bridge_y1 in wall_range and bridge_y2 in wall_range:
            self.current_wall.is_cracked = True
            self.current_wall_index += 1
            if self.current_wall_index < len(self.data_walls):
                self.current_wall = self.data_walls[self.current_wall_index]
            else:
                self.is_game_over = True
        else:
            self.reset_walls()


game = Game()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                game.check_if_data_crack()

    game.update()

    screen.fill("black")
    screen.blit(img_background,  (0, 0))
    draw_container()
    draw_bridge()
    game.draw_walls()
    game.draw_game_over()
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()