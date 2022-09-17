import game
import math
import pygame
from spawnable import Spawnable

class Enemy(Spawnable, pygame.sprite.Sprite):

    dist = 100
    name = ''

    def __init__(self, srf, x, y, color=(255, 0, 0), entangled=False, scale=1, speed=5):
        pygame.sprite.Sprite.__init__(self)
        Spawnable.__init__(self, srf, x, y)

        self.entangled = entangled
        self.speed = speed
        
        # Image 
        #img = pygame.image.load('graphics\Transperent\Icon1.png')
        #self.image = pygame.transform.scale(img, (img.get_width() * scale, img.get_height() * scale))
        #self.rect = self.image.get_rect()
        #self.rect.center = (x, y)

        # Rect only
        self.color = color
        self.rect = pygame.Rect(self.posX, self.posY, 60, 60)

    def clearBG(self):
        self.srf.fill((0, 0, 0, 0))

    def moveTowards(self, targetVect : list[int]):
        # Find direction vector (dx, dy) between enemy and player.
        dx = targetVect[0] - self.rect.x
        dy = targetVect[1] - self.rect.y
        dist = math.hypot(dx, dy)

        try:
            # Normalize.
            dx = dx / dist
            dy = dy / dist  
        except ZeroDivisionError: 
            return
        # Move along this normalized vector towards the player at current speed.
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
        self.clearBG()

    def draw(self, win):
        pygame.draw.rect(self.srf, self.color, self.rect)
        win.blit(self.srf, self.rect)

    def spawn(self):
        self.rect = pygame.Rect(self.posX, self.posY, 60, 60)
        game.enemyList.append(self)