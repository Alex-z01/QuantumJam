import pygame
import status_bars
from player import Player
from enemy import Enemy

pygame.init()

RUNNING = True
QUIT = True
SCREEN_W = 1080 
SCREEN_H = 720
SCREEN = pygame.display.set_mode((SCREEN_W, SCREEN_H))
FPS = 60
LEVEL = 1

#COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BACKGROUND = (207, 159, 255)

# IMAGES
PLAYER = 'graphics\Player\player_stand.png'
FLY1 = 'graphics\Fly\Fly1.png'
REDTRIANGLE = 'graphics/enemies/triangle/red triangle/redTriangle100.png'
BLUETRIANGLE = 'graphics/enemies/triangle/blue triangle/blueTriangle100.png'
WAVE = 'graphics/snail/snail1.png'

# PLAYER
playerSprite = Player(PLAYER)

# UI
health_bar = status_bars.health_bar(SCREEN, playerSprite)
level_display = status_bars.level_display(SCREEN)
game_over = status_bars.game_over(SCREEN, playerSprite, 600, 300, 300, 300)

# ENEMIES
redTriangle = Enemy(playerSprite, REDTRIANGLE, 3)
blueTriangle = Enemy(playerSprite, BLUETRIANGLE, 4)

# Groups
Player = pygame.sprite.GroupSingle()
Player.add(playerSprite)

Enemies = pygame.sprite.Group()
