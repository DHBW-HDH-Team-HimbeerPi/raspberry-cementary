import numpy as np
import random
from output_framework.output_framework import OutputFramework 

import SnakeController


pixelAmount = 16
pixelArray = np.full((pixelAmount , pixelAmount, 3), 0)
gameRunning = True
# pixelArray[10][10][1] = 255


def CreateGamefield():
    for x in pixelAmount-1:
        pixelArray[x][0][2] = 255
    for y in pixelAmount-1:
        pixelArray[0][y][2] = 255
    

def AppleSpawner():
    minDistance = 4;
    applePosX = random.randrange(1, 14)
    applePosY = random.randrange(1, 14)

    while(applePosX >= (SnakeController.posX + minDistance) and applePosX <= (SnakeController.posX - minDistance)):
        applePosX = random.randrange(1, 14)

    while(applePosY >= (SnakeController.posY + minDistance) and applePosY <= (SnakeController.posY - minDistance)):
        applePosY = random.randrange(1, 14)
    
    pixelArray[applePosX][applePosY][0] = 255


def main():

    CreateGamefield()
    AppleSpawner()

     OutputFramework.setWindow(pixelArray)

    while gameRunning:
        #code
        gameRunning = False

    
    if __name__ == "__main__":
        main()





    