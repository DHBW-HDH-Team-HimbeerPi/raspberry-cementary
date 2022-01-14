import numpy as np

class Player:

    def __init__(self, pixels, height, colorR, colorG, colorB):
        self.pixels = pixels
        self.height = height
        self.colorR = colorR
        self.colorG = colorG
        self.colorB = colorB

    def dimensions(self, height):
        pixelArray = np.full((self.pixels , self.pixels, 3), 0)
        for i in range(height):
            pixelArray[i][0][0] = self.colorR
            pixelArray[i][0][1] = self.colorG
            pixelArray[i][0][2] = self.colorB
        return pixelArray
