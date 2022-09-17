class Spawnable():
    srf = None
    posX, posY = 0, 0    
    
    def __init__(self, surface, x, y):
        self.srf = surface
        self.posX = x
        self.posY = y
    
    def setPos(self, x, y):
        self.posX = x
        self.posY = y

    def spawn(self):
        print("Spawned non-enemy")
        pass