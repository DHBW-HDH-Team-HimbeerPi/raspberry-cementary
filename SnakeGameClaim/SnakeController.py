import numpy as np

class SnakeController:

    pixelAmount = 16
    pixelArray = np.full((pixelAmount , pixelAmount, 3), 0)
    posX = [0]
    posY = [0]
    posXPrev = 0
    posYPrev = 0

    def __init__(self, posX, posY):
        self.posX[0] = posX
        self.posY[0] = posY
        self.posXPrev = 0
        self.posYPrev = 0

    def MoveSnake(self, direction: int):
        self.posYPrev = self.posY[len(self.posY)-1]
        self.posXPrev = self.posX[len(self.posX)-1]
        
        if (direction == 1):
            for i in range(0, len(self.posY)):
                self.posY[i] += 1
        elif (direction == 2):
            for i in range(0, len(self.posY)):
                self.posY[i] -= 1
        elif (direction == 3):
            for i in range(0, len(self.posX)):
                self.posX[i] -= 1
        elif (direction == 4):
            for i in range(0, len(self.posX)):
                self.posX[i] += 1

    def SnakeIsAlive(self):
        if ((self.posY[0] >= 15 or self.posY[0] <= 0) or (self.posX[0] >= 15 or self.posX[0] <= 0)):
            return False
        else:
            return True

    def EatApple(self):
        self.posX.append(self.posXPrev)
        self.posY.append(self.posYPrev)




        