from turtle import speed
import pygame
from sys import exit

pygame.init()

WIDTH, HEIGHT = 1080, 720
FPS = 60
BG = (180, 140, 230)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game')

clock = pygame.time.Clock()

# Define player action vars
moving_left = False
moving_right = False

def draw_bg():
    screen.fill(BG)

class Potion(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.speed = speed
        self.direction = 1
        self.flip = False
        img = pygame.image.load('graphics\Transperent\Icon1.png')
        self.image = pygame.transform.scale(img, (img.get_width() * scale, img.get_height() * scale))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move(self, moving_left, moving_right):
        # reset movement vars
        dx, dy = 0, 0

        # assign movement vars
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        # update rect pos
        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)



potion = Potion(200, 200, 3, 5)

run = True
while run:
    
    clock.tick(FPS)

    potion.draw()
    potion.move(moving_left, moving_right)

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