from turtle import Shape
import game
import player_class
import pygame
from shapes import Shapes
from spawner import Spawner
from enemy2 import Enemy2
from sys import exit
import status_bars


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

# Create a spawner
spawner = Spawner(screen)

# Create your enemy prefabs
triangleEnemy = Enemy2(Shapes.TRIANGLE, points=[(0, 0), (0, 100), (100, 0)])
squareEnemy = Enemy2(Shapes.SQUARE, color=(0,255,0), x=200, y=200)
squareEnemy2 = Enemy2(Shapes.SQUARE, color=(0,30,50), x=300, y=100)
squareEnemy3 = Enemy2(Shapes.SQUARE, color=(128,55,198), x=170, y=70)

# Spawn them
spawner.spawn(triangleEnemy, 1)
#spawner.spawn(squareEnemy, 1)
#spawner.spawn(squareEnemy2, 1)
#spawner.spawn(squareEnemy3, 1)

player = player_class.Player(80, 200)
health_bar = status_bars.health_bar(screen, player)
level_display = status_bars.level_display(screen)

while game.running:
    
    clock.tick(FPS)

    for element in game.enemyList:
        element.draw(screen)
        if element.shape == Shapes.SQUARE:
            element.moveRectTowards((10,200))

    for event in pygame.event.get():
        # Quit game
        if event.type == pygame.QUIT:
            game.running = False

    keys = pygame.key.get_pressed()
    player.do_player_things(screen, keys, pygame.mouse, [])
    health_bar.show_health()
    level_display.show_level()

    pygame.display.update()
    draw_bg()

pygame.quit()
exit()