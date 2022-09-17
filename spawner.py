import random
from enemy import Enemy
from spawnable import Spawnable

class Spawner():
    complete = False

    def __init__(self, win, surface):
        self.win = win
        self.srf = surface

    def spawn(self, obj, count):
        for i in range(count):
            if isinstance(obj, Spawnable):
                randX = random.randrange(0, 200)
                randY = random.randrange(0, 200)

                obj.setPos(randX, randY)
                print(obj.posX, " ", obj.posY)
                obj.spawn()


