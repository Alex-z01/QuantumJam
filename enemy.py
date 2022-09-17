from dis import dis
import pygame
import math

class Enemy(pygame.sprite.Sprite):

    dist = 100

    def __init__(self, win, x, y, scale, speed, entangled, color=(255, 0, 0)):
        pygame.sprite.Sprite.__init__(self)

        self.win = win
        self.speed = speed
        self.entangled = entangled

        # Image 
        #img = pygame.image.load('graphics\Transperent\Icon1.png')
        #self.image = pygame.transform.scale(img, (img.get_width() * scale, img.get_height() * scale))
        #self.rect = self.image.get_rect()
        #self.rect.center = (x, y)

        # Rect only
        self.color = color
        self.srf = pygame.Surface((win.get_width(), win.get_height()), pygame.SRCALPHA)
        self.rect = pygame.Rect(x, y, 60, 60)

    def clearBG(self):
        self.srf.fill((0, 0, 0, 0))

    def moveToTarget(self, target):
        # Find direction vector (dx, dy) between enemy and player.
        dx, dy = target.x - self.rect.x, target.y - self.rect.y
        dist = math.hypot(dx, dy)

        try:
            dx, dy = dx / dist, dy / dist  # Normalize.
        except ZeroDivisionError: 
            return
        # Move along this normalized vector towards the player at current speed.
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed



    def draw(self):
        self.clearBG()
        pygame.draw.rect(self.srf, self.color, self.rect)
        self.win.blit(self.srf, self.rect)