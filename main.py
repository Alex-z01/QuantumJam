import pygame
import enemySpawning
from sys import exit
from enemy import Enemy

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
e = Enemy(screen, 300, 300, 1, 5, False)
e2 = Enemy(screen, 30, 60, 1, 5, False, BLUE)

run = True
while run:
    
    clock.tick(FPS)

    e2.draw()

    #e.draw()
    #e.moveToTarget(e2.rect)

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