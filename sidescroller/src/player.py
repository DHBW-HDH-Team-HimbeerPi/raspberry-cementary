import numpy as np
import random as rand
from .spriteReader import readSprite, setPixelColor
from .sprites import Sprites
from .addObject import add

class Player():

    def __init__(self, pixelArray):
        self.amogus = readSprite(Sprites.player.value, False)
        self.colorR = rand.randrange(100, 255)
        self.colorG = rand.randrange(100, 255)
        self.colorB = rand.randrange(100, 255)
        self.posX = 0
        self.posY = 0
        add(pixelArray, self.dimensions(), 3, 0)

    def setPixelColor(self, pixelArray, x, y, r, g, b):
        pixelArray[x][y][0] = r
        pixelArray[x][y][1] = g
        pixelArray[x][y][2] = b
        pixelArray[x][y][3] = 1

    def setPixelColorSelf(self, pixelArray, x, y):
        self.setPixelColor(pixelArray, x, y, self.colorR, self.colorG, self.colorB)

    def dimensions(self):
        pixelArray = np.full((len(self.amogus), len(self.amogus[0]), 4), 0)
        for x in range(len(pixelArray)):
            for y in range(len(pixelArray[0])):
                if(int(self.amogus[x][y]) != 0):
                    pixelArray[x][y] = int(self.amogus[x][y])
                    if(int(self.amogus[x][y]) == 2):
                        self.setPixelColor(pixelArray, x, y, 0, 100, 255)
                        self.posX = x
                        self.posY = y
                    else:
                        self.setPixelColorSelf(pixelArray, x, y)
        return pixelArray

    def updatePosition(self, x, y):
        self.posX = x
        self.posY = y