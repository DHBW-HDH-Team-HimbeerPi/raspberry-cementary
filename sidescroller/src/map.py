from .spriteReader import readSprite
from .maps import Maps
from .addObject import add

class Map:
    def __init__(self):
        self.map = readSprite(Maps.mario.value, True)
        self.length = len(self.map)*16

    def updateMap(self, pixelArray, position):
        if(position<=self.length):
            if(position==4):
                add(pixelArray, self.map, False)
            else:
                add(pixelArray, self.map, True)



