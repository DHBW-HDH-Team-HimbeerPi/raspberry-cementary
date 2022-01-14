import numpy as np
import random as rand

class Player:

    
    def __init__(self, pixels):
        self.pixels = pixels
        self.colorR = rand.randrange(100, 255)
        self.colorG = rand.randrange(100, 255)
        self.colorB = rand.randrange(100, 255)

    def setPixel(self, pixelArray, x, y):
        pixelArray[x][y][0] = self.colorR
        pixelArray[x][y][1] = self.colorG
        pixelArray[x][y][2] = self.colorB
        pixelArray[x][y][3] = 1

    def setPixelBlue(self, pixelArray, x, y):
        pixelArray[x][y][0] = 0
        pixelArray[x][y][1] = 148
        pixelArray[x][y][2] = 255
        pixelArray[x][y][3] = 1

    def dimensions(self):
        pixelArray = np.full((self.pixels , self.pixels, 4), 0)
        self.setPixel(pixelArray, 15, 1)
        self.setPixel(pixelArray, 14, 1)
        self.setPixel(pixelArray, 15, 3)
        self.setPixel(pixelArray, 14, 3)
        self.setPixel(pixelArray, 13, 1)
        self.setPixel(pixelArray, 13, 3)
        self.setPixel(pixelArray, 14, 2)
        self.setPixel(pixelArray, 12, 2)
        self.setPixelBlue(pixelArray, 13, 2)
        
        return pixelArray