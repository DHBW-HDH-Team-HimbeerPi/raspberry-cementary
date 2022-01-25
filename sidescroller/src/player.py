import numpy as np
import random as rand
from .spriteReader import readSprite
from .sprites import Sprites

class Player:

    def __init__(self):
        self.amogus = readSprite(Sprites.amogus.value)
        self.colorR = rand.randrange(100, 255)
        self.colorG = rand.randrange(100, 255)
        self.colorB = rand.randrange(100, 255)

    def setPixelColor(self, pixelArray, x, y):
        pixelArray[x][y][0] = self.colorR
        pixelArray[x][y][1] = self.colorG
        pixelArray[x][y][2] = self.colorB
        pixelArray[x][y][3] = 1

    def dimensions(self):
        pixelArray = np.full((16 , 16, 4), 0)
        for x in range(0, len(pixelArray)):
            for y in range(0, len(pixelArray[0])):
                if(int(self.amogus[x][y]) != 0):
                    pixelArray[x][y] = int(self.amogus[x][y])
                    self.setPixelColor(pixelArray, x, y)
        return pixelArray