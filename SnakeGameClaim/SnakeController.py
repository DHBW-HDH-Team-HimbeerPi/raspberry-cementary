from http.client import SWITCHING_PROTOCOLS
import numpy as np

class SnakeController:

    def __init__(self, posX, posY):
        colorR = 0
        colorG = 255
        colorB = 0
        self.posX = posX
        self.posY = posY

    def MoveSnake(self, direction: int):
        # match direction:
        #     case 1:
        #         self.posY += 1
        #     case 2:
        #         self.posY -= 1
        #     case 3: 
        #         self.posX += 1
        #     case 4:
        #         self.posX -= 1
                
        if (direction == 1):
            self.posY = 1
        elif (direction == 2):
            self.posY = -1
        elif (direction == 3):
            self.posX = 1
        elif (direction == 4):
            self.posX = -1
        