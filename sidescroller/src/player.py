import numpy as np
import random as rand
from .spriteReader import readSprite

class Player:

    def __init__(self):

        self.amogus = readSprite("amogus.csv")
        self.colorR = rand.randrange(100, 255)
        self.colorG = rand.randrange(100, 255)
        self.colorB = rand.randrange(100, 255)

    def setPixel(self, pixelArray, x, y):
        pixelArray[x][y][0] = self.colorR
        pixelArray[x][y][1] = self.colorG
        pixelArray[x][y][2] = self.colorB
        pixelArray[x][y][3] = 1

    def dimensions(self):
        pixelArray = np.full((16 , 16, 4), 0)
        for i in range(0, len(pixelArray)):
            for j in range(0, len(pixelArray[0])):
                self.setPixel(pixelArray, i, j)
                pixelArray[i][j] = self.amogus[i][j]
        return pixelArray