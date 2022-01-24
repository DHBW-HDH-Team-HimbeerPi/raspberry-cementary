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
        
        minDistance = 3;
        self.posX = random.randrange(1, 14)
        self.posY = random.randrange(1, 14)

        while((self.posX <= (snakeController.posX[0] + minDistance) and self.posX >= (snakeController.posX[0] - minDistance)) and self.AppleInSnake(snakeController, "X") == False):
            self.posX = random.randrange(1, 14)

        while((self.posY <= (snakeController.posY[0] + minDistance) and self.posY >= (snakeController.posY[0] - minDistance)) and self.AppleInSnake(snakeController, "Y") == False):
            self.posY = random.randrange(1, 14)

        self.pixelArray[self.posX][self.posY][0] = 255

        if (self.posXPrev == 0):
            self.posX = 3
            self.posY = 10

        applePosition = [self.posX, self.posY, self.posXPrev, self.posYPrev]
        return applePosition


    def AppleInSnake(self, sc, direc):
        if (direc == "X"):
            for i in range(0, len(sc.posX)):
                if (sc.posX[i] == self.posX):
                    return True
        elif (direc == "Y"):
            for i in range(0, len(sc.posY)):
                if (sc.posY[i] == self.posY):
                    return True
        
        return False
