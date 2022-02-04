import numpy as np
import random

class Apple():


    posXPrev = 0
    posYPrev = 0
    pixelAmount = 16
    pixelArray = np.full((pixelAmount , pixelAmount, 3), 0)

    def __init__(self):
        self.posX = 0
        self.posY = 0


    def AppleSpawner(self, snakeController):
        self.posXPrev = self.posX
        self.posYPrev = self.posY
        
        self.posX = random.randrange(1, 15)
        self.posY = random.randrange(1, 15)

        while(self.AppleNotInSnake(snakeController)):
            self.posX = random.randrange(1, 15)
            self.posY = random.randrange(1, 15)

        self.pixelArray[self.posX][self.posY][0] = 255

        if (self.posXPrev == 0):
            self.posX = 3
            self.posY = 10

        applePosition = [self.posX, self.posY, self.posXPrev, self.posYPrev]
        return applePosition


    def AppleNotInSnake(self, sc):
        for i in range(0, len(sc.posX)):
            if (sc.posX[i] == self.posX and sc.posY[i] == self.posY):
                return True
        
        return False
