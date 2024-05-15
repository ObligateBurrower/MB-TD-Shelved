import pygame
import math


class Enemy:
    def __init__(self, path, image, start_pos):
        self.path = path
        self.path_index = 0
        self.position = start_pos
        self.image = image
        self.active = True
        self.reached_end = False  # To indicate if the enemy reached the end

    def move(self):
        if self.path_index < len(self.path):
            target = self.path[self.path_index]
            distance = math.hypot(target[0] - self.position[0], target[1] - self.position[1])
            if distance < 2:
                self.path_index += 1
                if self.path_index == len(self.path):
                    self.active = False
                    self.reached_end = True  # Set this flag when the end is reached
            else:
                angle = math.atan2(target[1] - self.position[1], target[0] - self.position[0])
                self.position = (
                    self.position[0] + 2 * math.cos(angle),
                    self.position[1] + 2 * math.sin(angle)
                )

    def draw(self, surface):
        if self.active:
            surface.blit(self.image, self.position)


class Display:
    def __init__(self, font_name='grand9kpixelregular', font_size=24, initial_health=50):
        pygame.font.init()
        self.font = pygame.font.SysFont(font_name, font_size)
        self.health = initial_health

    def update_health(self, new_health):
        self.health = new_health

    def draw(self, surface):
        health_text = self.font.render(f'Health: {self.health}', True, (255, 255, 255))
        surface.blit(health_text, (10, 10))


def base_map(scale_x, scale_y):
    gameDisplay.blit(mapImg, (scale_x, scale_y))


# Initialize Pygame
pygame.init()
display_width, display_height = 320, 320
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("MouthBalls TD")
clock = pygame.time.Clock()
crashed = False

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Initialize HUD
hud = Display(initial_health=50)

# Load assets
mapImg = pygame.image.load("C:/Users/justi/OneDrive/Documents/Pixel art/Tutorial/td_assets/map mockup.png")
enemyImg = pygame.image.load("C:/Users/justi/OneDrive/Documents/Pixel art/Tutorial/td_assets/enemy.png")
enemyPath = [(15, 35), (75, 35), (75, 75), (35, 75), (35, 295), (75, 295), (75, 195),
             (145, 195), (145, 155), (75, 155), (75, 115), (115, 115), (115, 15), (195, 15),
             (195, 55), (155, 55), (155, 115), (195, 115), (195, 235), (115, 235), (115, 275),
             (235, 275), (235, 35), (275, 35), (275, 275), (295, 275)]

enemies = []
spawn_interval = 250
last_spawn_time = pygame.time.get_ticks()
max_enemies = 10

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    current_time = pygame.time.get_ticks()
    if len(enemies) < max_enemies and current_time - last_spawn_time > spawn_interval:
        enemies.append(Enemy(enemyPath, enemyImg, enemyPath[0]))
        last_spawn_time = current_time

    gameDisplay.fill(black)
    base_map(0, 0)
    for enemy in enemies:
        enemy.move()
        enemy.draw(gameDisplay)
        if enemy.reached_end:
            hud.update_health(hud.health - 1)  # Update health via Display class
            enemies.remove(enemy)

    hud.draw(gameDisplay)  # Draw HUD elements including health

    pygame.display.update()
    clock.tick(60)

pygame.quit()
