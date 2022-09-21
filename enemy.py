from distutils.spawn import spawn
import math
import random
import pygame
import GLOBALS

class Enemy(pygame.sprite.Sprite):
    def __init__(self, target, image, speed):
        pygame.sprite.Sprite.__init__(self)

        self.image_loc = image
        self.image = pygame.image.load(self.image_loc)

        centerX = random.randrange(0, GLOBALS.SCREEN_W)
        centerY = random.randrange(0, GLOBALS.SCREEN_H)

        self.rect = self.image.get_rect(center=(centerX, centerY))
        self.pos = (centerX, centerY)

        self.target = target
        self.speed = speed

        self.maxHP = 20
        self.currentHP = self.maxHP
        self.damage = 5

        self.time_since_last_attack = 0
        self.attack_delay = 1000 #ms
    
    def getCurrentHP(self):
        return self.currentHP

    def getMaxHP(self):
        return self.maxHP

    def getDMG(self):
        return self.damage

    def setCurrentHP(self, hp):
        self.currentHP = hp
    
    def setMaxHP(self, hp):
        self.maxHP = hp

    def moveTo(self, target):
        # Find direction vector (dx, dy) between enemy and player.
        dx = target.rect.centerx - self.rect.centerx
        dy = target.rect.centery - self.rect.centery
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

    def TakeDamage(self, damage):
        print("Ouch")
        if self.currentHP - damage <= 0:
            self.Die()
        self.setCurrentHP(self.currentHP - damage)

    def Die(self):
        self.kill()
        self.isWaveOver()
        return

    def isWaveOver(self):
        print(len(GLOBALS.Enemies))
        if len(GLOBALS.Enemies) == 0:
            GLOBALS.LEVEL += 1
            GLOBALS.level_display.set_level(GLOBALS.LEVEL)

    def checkCollisions(self):
        collisions = pygame.sprite.spritecollide(self, GLOBALS.Player, False)
        self.currentTime = pygame.time.get_ticks()

        if self.currentTime - self.time_since_last_attack >= self.attack_delay:
            for col in collisions:
                col.TakeDamage(self.damage)
                self.time_since_last_attack = self.currentTime

    def update(self):
        self.checkCollisions()
        self.moveTo(self.target)