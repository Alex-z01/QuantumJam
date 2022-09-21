import pygame
import GLOBALS
from enemy import Enemy

class EnemySpawner():
    def __init__(self, enemy, count):

        self.target = enemy.target
        self.image_loc = enemy.image_loc
        self.speed = enemy.speed
        self.count = count
        self.spawned = False
        
    def spawn(self):
        for i in range(self.count):
            newEnemy = Enemy(self.target, self.image_loc, self.speed)
            GLOBALS.Enemies.add(newEnemy)
        self.spawned = True