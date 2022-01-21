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
        minDistance = 3;
        self.posX = random.randrange(1, 14)
        self.posY = random.randrange(1, 14)

        while(self.posX <= (snakeController.posX + minDistance) and self.posX >= (snakeController.posX - minDistance)):
            self.posX = random.randrange(1, 14)

        while(self.posY <= (snakeController.posY + minDistance) and self.posY >= (snakeController.posY - minDistance)):
            self.posY = random.randrange(1, 14)
    
        self.posXPrev = self.posX
        self.posYPrev = self.posY

        self.pixelArray[self.posX][self.posY][0] = 255

        applePosition = [self.posX, self.posY, self.posXPrev, self.posYPrev]
        return applePosition