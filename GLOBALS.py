import pygame
from player import Player
from enemy import Enemy

SCREEN_W = 1080 
SCREEN_H = 720
SCREEN = pygame.display.set_mode((SCREEN_W, SCREEN_H))
FPS = 60

#COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# IMAGES
PLAYER = 'graphics\Player\player_stand.png'
FLY1 = 'graphics\Fly\Fly1.png'
TRIANGLE100 = 'graphics/enemies/triangle/red triangle/redTriangle100.png'
WAVE = 'graphics/snail/snail1.png'

# Groups
playerSprite = Player(PLAYER)

Player = pygame.sprite.GroupSingle()
Player.add(playerSprite)

Enemies = pygame.sprite.Group()
for i in range(5):
    Enemies.add(Enemy(playerSprite, TRIANGLE100, 3))