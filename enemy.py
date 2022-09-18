import math
import pygame

class Enemy(pygame.sprite.Sprite):
    def __init__(self, target, speed):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("graphics/enemies/triangle/red triangle/redTriangle100%.png").convert_alpha()

        centerX = self.image.get_rect().centerx
        centerY = self.image.get_rect().centery

        self.rect = self.image.get_rect(center=(0, 0))

        self.target = target
        self.speed = speed
    
    def moveTo(self, target):
        # Find direction vector (dx, dy) between enemy and player.
        dx = target.get_rectangle().centerx - self.rect.centerx
        dy = target.get_rectangle().centery - self.rect.centery
        dist = math.hypot(dx, dy)

        # Move along this normalized vector towards the player at current speed.
        if dist > dx:
            dx = dx / dist
            self.rect.centerx += dx * self.speed
        else:
            self.rect.centerx += dx * self.speed

        if dist > dx:
            dy = dy / dist
            self.rect.centery += dy * self.speed  
        else:
            self.rect.centery += dy * self.speed     

    def update(self):
        self.moveTo(self.target)