from turtle import pos
import game
import pygame
import math
from shapes import Shapes

class Enemy2():
    def __init__(self, shape, color=(255, 0, 0), points : list[pygame.Vector2] = None, radius=None, pos : pygame.Vector2 = None):

        # Stats
        self.maxHP = 0
        self.currentHP = self.maxHP
        self.damage = 0
        self.speed = 5

        # Data
        self.shape = shape
        self.points = points
        self.color = color
        self.radius = radius
        self.pos = pos
        self.rect = None

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

    def getRect(self):
        return self.rect

    def getPos(self):
        return self.pos

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

    def updateRect(self, pos : pygame.Vector2):
        self.rect.x = pos[0]
        self.rect.y = pos[1]

    def clearBG(self):
        EMPTY = pygame.Color(0,0,0,0)
        self.srf.fill(EMPTY)

    def moveRectTowards(self, targetVect : list[int]):
        posX, posY = self.pos[0], self.pos[1]
        # Find direction vector (dx, dy) between enemy and player.
        dx = targetVect[0] - posX
        dy = targetVect[1] - posY
        dist = math.hypot(dx, dy)

        if dist > dx and dist > dy:
            try:
                # Normalize.
                dx = dx / dist
                dy = dy / dist  
            except ZeroDivisionError: 
                return
            # Move along this normalized vector towards the player at current speed.
            posX += dx * self.speed
            posY += dy * self.speed   
            self.pos = [posX, posY]         
        self.clearBG()

    def moveRect(self, targetVect : pygame.Vector2):
         # Find direction vector (dx, dy) between enemy and player.
        dx = targetVect[0] - self.rect.x
        dy = targetVect[1] - self.rect.y
        dist = math.hypot(dx, dy)

        if dist > dx and dist > dx:
            try:
                # Normalize.
                dx = dx / dist
                dy = dy / dist  
            except ZeroDivisionError: 
                return
            # Move along this normalized vector towards the player at current speed.
            self.rect.x += dx * self.speed
            self.rect.y += dy * self.speed            
        #self.clearBG()       

    def setPoints(self):
        newPoints = []

        for point in self.points:
            newTuple = [point[0] + 1, point[1] - 1]
            newPoints.append(newTuple)
        
        self.points = newPoints
        self.clearBG()

    def draw(self, screen):
        if self.shape == Shapes.CIRCLE:
            self.rect = pygame.draw.circle(self.srf, self.color, radius=self.radius)
            screen.blit(self.srf, self.rect)
            return
        if self.shape == Shapes.TRIANGLE:
            if self.rect == None:
                self.rect = pygame.draw.polygon(self.srf, self.color, self.points)
            screen.blit(self.srf, self.rect)
            return
        if self.shape == Shapes.SQUARE:
            self.rect = pygame.Rect(self.pos[0], self.pos[1], 60, 60)
            self.rect = pygame.draw.rect(self.srf, self.color, self.rect)
            screen.blit(self.srf, self.rect)
            return

    def spawn(self):
        game.enemyList.append(self)