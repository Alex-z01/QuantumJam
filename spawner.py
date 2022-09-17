import pygame
from enemy2 import Enemy2
from shapes import Shapes

class Spawner():
    complete = False

    def __init__(self, screen):
        self.screen = screen
        self.srf = pygame.Surface((screen.get_width(), screen.get_height()), pygame.SRCALPHA)

    def spawn(self, obj, count):
        self.srf = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)
        for i in range(count):
            # CIRCLE
            if obj.shape == Shapes.CIRCLE:
                thing = Enemy2(obj.shape, color=obj.color, radius=obj.radius)
                thing.setSurface(self.srf)
                thing.spawn()
            # TRIANGLE
            if obj.shape == Shapes.TRIANGLE:
                thing = Enemy2(obj.shape, color=obj.color, points=obj.points)
                thing.setSurface(self.srf)
                thing.spawn()
            # SQUARE
            if obj.shape == Shapes.SQUARE:
                thing = Enemy2(obj.shape, color=obj.color, x=obj.posX, y=obj.posY)
                thing.setSurface(self.srf)
                thing.spawn()
                