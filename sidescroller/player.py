import numpy as np

class Player:

    def __init__(self, pixels, height, colorR, colorG, colorB):
        self.pixels = pixels
        self.height = height
        self.colorR = colorR
        self.colorG = colorG
        self.colorB = colorB

    def dimensions(self):
        pixelArray = np.full((self.pixels , self.pixels, 4), 0)
        for i in range(self.height):
            pixelArray[self.pixels-i-1][2][0] = self.colorR
            pixelArray[self.pixels-i-1][2][1] = self.colorG
            pixelArray[self.pixels-i-1][2][2] = self.colorB
            pixelArray[self.pixels-i-1][2][3] = 1
        return pixelArray
