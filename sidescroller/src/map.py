from .spriteReader import dimensions, readSprite
from .sprites import numberToSprite
from .maps import Maps
from .addObject import add
import math
import numpy as np

class Map:

    def __init__(self, pixelArray):
        self.map = readSprite(Maps.mario.value, True)
        self.length = int((len(self.map[0])/4)*16) #length in pixels
        self.initialMap(pixelArray)

    def initialMap(self, pixelArray):
        pixels = 4
        for x in range(pixels):
            for y in range(pixels+4):
                spriteNumber = int(self.map[x][y])
                if spriteNumber != 0:
                    sprite = numberToSprite(spriteNumber)
                    add(pixelArray, dimensions(sprite), x, y)


    def mapToArray(self, position):
        pixels = 4
        pos = math.floor(position/16)
        print(pos)
        pixelArray = np.full((pixels, pixels, 4), 0)

    def updateMap(self, pixelArray, position):
        if position<=self.length-1 and position > 2:
            print("test")
            #add(pixelArray, self.mapToArray(position), 3, 1, True)





