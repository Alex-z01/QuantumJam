import game
import pygame
import math
from shapes import Shapes

class Enemy2():
    def __init__(self, shape, points : list[pygame.Vector2] = None, color=(255, 0, 0), radius=None, x=0, y=0):

        # Stats
        self.maxHP = 0
        self.currentHP = self.maxHP
        self.damage = 0
        self.speed = 1

        # Data
        self.shape = shape
        self.points = points
        self.color = color
        self.radius = radius
        self.posX = x
        self.posY = y

    def getCurrentHP(self):
        return self.currentHP

    def getMaxHP(self):
        return self.maxHP

    def getDMG(self):
        return self.damage

    def getShape(self):
        return self.shape
    
    def getSurface(self):
        return self.srf
    
    def getRadius(self):
        return self.radius

    def getPoints(self):
        return self.points

    def getPos(self):
        return [self.posX, self.posY] 

    def setPos(self, pos : pygame.Vector2):
        self.posX = pos[0]
        self.posY = pos[1]

    def setColor(self, color : pygame.color):
        self.color = color

    def setSurface(self, srf):
        self.srf = srf

    def setCurrentHP(self, hp):
        self.currentHP = hp
    
    def setMaxHP(self, hp):
        self.maxHP = hp

    def clearBG(self):
        EMPTY = pygame.Color(0,0,0,0)
        self.srf.fill(EMPTY)

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

    def draw(self, screen):
        if self.shape == Shapes.CIRCLE:
            RECT = pygame.draw.circle(self.srf, self.color, radius=self.radius)
            screen.blit(self.srf, RECT)
            return
        if self.shape == Shapes.TRIANGLE:
            RECT = pygame.draw.polygon(self.srf, self.color, self.points)
            screen.blit(self.srf, RECT)
            return
        if self.shape == Shapes.SQUARE:
            RECT = pygame.Rect(self.posX, self.posY, 60, 60)
            RECT = pygame.draw.rect(self.srf, self.color, RECT)
            screen.blit(self.srf, RECT)
            return

    def spawn(self):
        game.enemyList.append(self)