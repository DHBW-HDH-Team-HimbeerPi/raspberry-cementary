import numpy as np
import random as rand
from .spriteReader import readSprite, setPixelColor
from .sprites import Sprites

class Player:

    def __init__(self):
        self.amogus = readSprite(Sprites.amogus.value)
        self.colorR = rand.randrange(100, 255)
        self.colorG = rand.randrange(100, 255)
        self.colorB = rand.randrange(100, 255)

    def setPixelColor(self, pixelArray, x, y, r, g, b):
        pixelArray[x][y][0] = r
        pixelArray[x][y][1] = g
        pixelArray[x][y][2] = b
        pixelArray[x][y][3] = 1

    def setPixelColorSelf(self, pixelArray, x, y):
        self.setPixelColor(pixelArray, x, y, self.colorR, self.colorG, self.colorB)

    def dimensions(self):
        pixelArray = np.full((16 , 16, 4), 0)
        for x in range(0, len(pixelArray)):
            for y in range(0, len(pixelArray[0])):
                if(int(self.amogus[x][y]) != 0):
                    pixelArray[x][y] = int(self.amogus[x][y])
                    if(int(self.amogus[x][y]) == 2):
                        self.setPixelColor(pixelArray, x, y, 0, 100, 255)
                    else:
                        self.setPixelColorSelf(pixelArray, x, y)
        return pixelArray