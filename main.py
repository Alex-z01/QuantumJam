import game
import pygame
import GLOBALS
import status_bars
from sys import exit

pygame.init()

BG = GLOBALS.BLUE

pygame.display.set_caption('Game')

clock = pygame.time.Clock()

def draw_bg():
    GLOBALS.SCREEN.fill(BG)

health_bar = status_bars.health_bar(GLOBALS.SCREEN, GLOBALS.playerSprite)
level_display = status_bars.level_display(GLOBALS.SCREEN)
game_over = status_bars.game_over(GLOBALS.SCREEN, GLOBALS.playerSprite, 600, 300, 300, 300)

while game.running:
    
    clock.tick(GLOBALS.FPS)

    keys = pygame.key.get_pressed()

    GLOBALS.Player.draw(GLOBALS.SCREEN)
    GLOBALS.Player.update(keys)
    GLOBALS.Enemies.draw(GLOBALS.SCREEN)
    GLOBALS.Enemies.update()

    for event in pygame.event.get():
        # Quit game
        if event.type == pygame.QUIT:
            game.running = False

    health_bar.show_health()
    level_display.show_level()
    #game_over.show()

    pygame.display.update()
    draw_bg()

pygame.quit()
exit()