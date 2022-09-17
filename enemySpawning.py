from locale import currency
import pygame

class Spawner():
    current = 0

    def __init__(self, obj, count, repeat, time):
        self.obj = obj
        self.count = count 
        self.repeat = repeat
        self.time = time

    def spawn(self, srf, obj):
        for i in range(self.count):
            pygame.draw.rect(srf, (0, 255, 0), obj)
        self.current += 1

    
srf = pygame.Surface((1080, 720), pygame.SRCALPHA)
rect = pygame.Rect(0, 0, 30, 30)

spawner = Spawner(rect, 1, 3, 1)

while spawner.current < spawner.repeat:
    spawner.spawn(srf, rect)
    print("Spawning")


