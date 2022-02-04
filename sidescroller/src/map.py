from .spriteReader import readSprite
from .maps import Maps

class Map:
    def __init__(self):
        self.map = readSprite(Maps.mario.value, True)

    def updateMap(self, pixelArray):
        print(len(self.map))


