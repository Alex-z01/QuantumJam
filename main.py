import pygame
import GLOBALS
import spawning
from sys import exit

BG = GLOBALS.BACKGROUND

pygame.display.set_caption('Game')

clock = pygame.time.Clock()

def draw_bg():
    GLOBALS.SCREEN.fill(BG)

while GLOBALS.RUNNING:
    
    clock.tick(GLOBALS.FPS) 

    print(f"Current enemy count {len(GLOBALS.Enemies)}, wave {GLOBALS.LEVEL}")

    try:
        if spawning.waves[GLOBALS.LEVEL-1].spawned == False:
            spawning.waves[GLOBALS.LEVEL-1].spawn()
    except IndexError:
        print("YOU WON!")
        GLOBALS.RUNNING = False
        GLOBALS.QUIT = False


    keys = pygame.key.get_pressed()

    GLOBALS.Player.draw(GLOBALS.SCREEN)
    GLOBALS.Player.update(keys)
    GLOBALS.Enemies.draw(GLOBALS.SCREEN)
    GLOBALS.Enemies.update()

    for event in pygame.event.get():
        # Quit game
        if event.type == pygame.QUIT:
            GLOBALS.RUNNING = False

    GLOBALS.health_bar.show_health()
    GLOBALS.level_display.show_level()
    #game_over.show()

    pygame.display.update()
    draw_bg()

if GLOBALS.QUIT == True:
    pygame.quit()
    exit()