import pygame
import math


class Enemy:
    def __init__(self, path, image, start_pos):
        self.path = path
        self.path_index = 0
        self.position = start_pos
        self.image = image
        self.active = True

    def move(self):
        if self.path_index < len(self.path):
            target = self.path[self.path_index]
            distance = math.hypot(target[0] - self.position[0], target[1] - self.position[1])

            if distance < 2:
                self.path_index += 1  # Move to next waypoint if close enough
                if self.path_index == len(self.path):
                    self.active = False  # Deactivate when the end is reached
            else:
                angle = math.atan2(target[1] - self.position[1], target[0] - self.position[0])
                self.position = (
                    self.position[0] + 2 * math.cos(angle),
                    self.position[1] + 2 * math.sin(angle)
                )

    def draw(self, surface):
        if self.active:
            surface.blit(self.image, self.position)


def base_map(scale_x, scale_y):
    gameDisplay.blit(mapImg, (scale_x, scale_y))


# Initialize Pygame
pygame.init()

# Game window setup
display_width = 320
display_height = 320

# dimensions for the game
gameDisplay = pygame.display.set_mode((display_width, display_height))

# set the title for the game
pygame.display.set_caption("MouthBalls TD")

# instantiate the clock in order to set the game's FPS.
clock = pygame.time.Clock()

# declare the game as not crashed
crashed = False

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Load assets
mapImg = pygame.image.load("C:/Users/justi/OneDrive/Documents/Pixel art/Tutorial/td_assets/map mockup.png")
enemyImg = pygame.image.load("C:/Users/justi/OneDrive/Documents/Pixel art/Tutorial/td_assets/enemy.png")

# the waypoints needed for the path that the enemies follow
enemyPath = [(15, 35), (75, 35), (75, 75), (35, 75), (35, 295), (75, 295), (75, 195),
             (145, 195), (145, 155), (75, 155), (75, 115), (115, 115), (115, 15), (195, 15),
             (195, 55), (155, 55), (155, 115), (195, 115), (195, 235), (115, 235), (115, 275),
             (235, 275), (235, 35), (275, 35), (275, 275), (295, 275)]

# a place to hold all enemies
enemies = []
spawn_interval = 250
last_spawn_time = pygame.time.get_ticks()
max_enemies = 10

# as long as the game is running, keep going.
while not crashed:
    for event in pygame.event.get():  # reads the events as they happen
        if event.type == pygame.QUIT:  # if the game is quit, quit the game
            crashed = True  # crash the game

    current_time = pygame.time.get_ticks()
    if len(enemies) < max_enemies and current_time - last_spawn_time > spawn_interval:
        enemies.append(Enemy(enemyPath, enemyImg, enemyPath[0]))
        last_spawn_time = current_time

    # if not crashed, display the game
    gameDisplay.fill(black)  # fill the background with black
    base_map(0, 0)  # load the game map
    for enemy in enemies:
        enemy.move()
        enemy.draw(gameDisplay)

    # update the display
    pygame.display.update()
    clock.tick(60)  # keep the game at 60FPS

pygame.quit()
quit()
