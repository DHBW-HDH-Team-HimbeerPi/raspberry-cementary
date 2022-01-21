import numpy as np

class SnakeController:

    pixelAmount = 16
    pixelArray = np.full((pixelAmount , pixelAmount, 3), 0)
    posX = 0
    posY = 0
    posXOld = 0
    posYOld = 0

    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY
        self.posXOld = 0
        self.posYOld = 0

    def MoveSnake(self, direction: int):
        self.posYOld = self.posY
        self.posXOld = self.posX
        
        if (direction == 1):
            self.posY += 1
        elif (direction == 2):
            self.posY -= 1
        elif (direction == 3):
            self.posX -= 1
        elif (direction == 4):
            self.posX += 1

    def SnakeIsAlive(self):
        if ((self.posY >= 15 or self.posY <= 0) or (self.posX >= 15 or self.posX <= 0)):
            return False
        else:
            return True




        