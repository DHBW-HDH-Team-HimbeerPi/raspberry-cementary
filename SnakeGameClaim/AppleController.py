from multiprocessing.dummy import Array
from ssl import ALERT_DESCRIPTION_ILLEGAL_PARAMETER
import numpy as np
import random

from pygame import pixelarray

class Apple():

    pixelAmount = 16
    pixelArray = np.full((pixelAmount , pixelAmount, 3), 0)

    def __init__(self):
        self.posX = 0
        self.posY = 0

    def AppleSpawner(self, snakeController):
        minDistance = 4;
        self.posX = random.randrange(1, 14)
        self.posY = random.randrange(1, 14)

        while(self.posX >= (snakeController.posX + minDistance) and self.posX <= (snakeController.posX - minDistance)):
            self.posX = random.randrange(1, 14)

        while(self.posY >= (snakeController.posY + minDistance) and self.posY <= (snakeController.posY - minDistance)):
            self.posY = random.randrange(1, 14)
    
        self.pixelArray[self.posX][self.posY][0] = 255
        applePosition = [self.posX, self.posY]
        return applePosition