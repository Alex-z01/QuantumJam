import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1080, 720))
pygame.display.set_caption('Game')
clock = pygame.time.Clock()



surface = pygame.Surface((100, 200))
surface.fill('White')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
   
    screen.blit(surface, (0, 0))

    pygame.display.update()
    clock.tick(60)
