import game
import pygame
import random
from spawnable import Spawnable
from spawner import Spawner
from enemy import Enemy
from sys import exit

pygame.init()

WIDTH, HEIGHT = 1080, 720
FPS = 60
BG = (180, 140, 230)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game')

clock = pygame.time.Clock()

def draw_bg():
    screen.fill(BG)

BLUE = (0, 0, 255)

spawnerSurface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

otherObject = Spawnable(spawnerSurface, 0, 0)
squareEnemy = Enemy(spawnerSurface, 0, 0)

spawner = Spawner(screen, spawnerSurface)
spawner.spawn(squareEnemy, 3)

run = True
while run:
    
    clock.tick(FPS)

    for element in game.enemyList:
        element.draw(screen)
        element.moveTowards((0, 0))

    for event in pygame.event.get():
        # Quit game
        if event.type == pygame.QUIT:
            run = False

        # Keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_ESCAPE:
                run = False

        # Keyboard release
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False

    pygame.display.update()
    draw_bg()

pygame.quit()
exit()