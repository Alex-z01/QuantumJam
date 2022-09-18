from glob import glob
import game
import player_class
import pygame
import GLOBALS
from enemy import Enemy
from shapes import Shapes
from spawner import Spawner
from enemy2 import Enemy2
from sys import exit
import status_bars

pygame.init()

BG = GLOBALS.BLUEd

screen = pygame.display.set_mode((GLOBALS.SCREEN_W, GLOBALS.SCREEN_H))
pygame.display.set_caption('Game')

clock = pygame.time.Clock()

def draw_bg():
    screen.fill(BG)

player = player_class.Player(80, 200)
health_bar = status_bars.health_bar(screen, player)
level_display = status_bars.level_display(screen)
game_over = status_bars.game_over(screen, player, 600, 300, 300, 300)

Enemies = pygame.sprite.Group()
Enemies.add(Enemy(player, 3))

while game.running:
    
    clock.tick(GLOBALS.FPS)

    Enemies.draw(screen)
    Enemies.update()

    for event in pygame.event.get():
        # Quit game
        if event.type == pygame.QUIT:
            game.running = False

    keys = pygame.key.get_pressed()
    player.do_player_things(screen, keys, pygame.mouse, Enemies.sprites(), game.projectileList)
    health_bar.show_health()
    level_display.show_level()
    game_over.show()

    pygame.display.update()
    draw_bg()

pygame.quit()
exit()