from .spriteReader import readSprite
from .maps import Maps
from .addObject import add
import math
import numpy as np
class Map:

    def __init__(self):
        self.map = readSprite(Maps.mario.value, True)
        self.length = len(self.map)*16

    def mapToArray(self, position):
        pixels = 16
        pos = math.floor(position/pixels)
        pixelArray = np.full((pixels, pixels, 4), 0)
        for x in range(pixels):
            for y in range(pixels):
                if()


    def updateMap(self, pixelArray, position):
        if(position<=self.length):
            if(position==2):
                add(pixelArray, self.mapToArray(position), False)
            #else:
                #add(pixelArray, self.map, True)





