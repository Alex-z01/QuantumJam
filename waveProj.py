import pygame
import math
import GLOBALS

class Wave(pygame.sprite.Sprite):
    def __init__(self, x, y, image, angle, wave_growth=1.01):
        pygame.sprite.Sprite.__init__(self)

        self.image_loc = image
        self.image = pygame.image.load(self.image_loc)

        self.rect = self.image.get_rect(center=(x, y))
        		
        self.angle = angle
        self.speed = 10
        self.damage = 5
        self.wave_growth = wave_growth

    def move(self):
        self.rect.left += self.speed * math.cos(math.radians(self.angle))
        self.rect.top += self.speed * math.sin(math.radians(self.angle))

    def checkCollisions(self):
        collisions = pygame.sprite.spritecollide(self, GLOBALS.Enemies, False)
        for col in collisions:
            self.kill()
            col.TakeDamage(self.damage)

    def update(self):
        self.checkCollisions()
        self.move()
    