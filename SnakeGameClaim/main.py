import time
from tokenize import Name
import numpy as np
import random
try:
    from output_framework.output_framework import OutputFramework 
    print("outputFramework detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicorn

from SnakeController import SnakeController
from AppleController import Apple


sc = SnakeController(3, 6)
apple = Apple()
pixelAmount = 16
pixelArray = np.full((pixelAmount , pixelAmount, 3), 0)
gameRunning = True

def CreateGamefield():
    for x in range(0, pixelAmount):
        pixelArray[x][0][2] = 255
    for y in range(0, pixelAmount):
        pixelArray[0][y][2] = 255

    for x in range(0, pixelAmount):
        pixelArray[x][15][2] = 255
    for y in range(0, pixelAmount):
        pixelArray[15][y][2] = 255
    

def DisplaySimulation():
    for i in range(0, 16):
        for j in range(0, 16):
            unicorn.set_pixel(i, j, pixelArray[i][j][0],  pixelArray[i][j][1],  pixelArray[i][j][2])
    unicorn.show()

def DisplayApple(i):
    applePosXY = apple.AppleSpawner(sc)
    pixelArray[applePosXY[0]][applePosXY[1]][0] = 255

    if ((applePosXY[2] != 0 or applePosXY[3] != 0) and i == 1):
        pixelArray[applePosXY[2]][applePosXY[3]][0] = 0


def main():

    gameRunning = True
    CreateGamefield()
    DisplayApple(0)

    
    try:
        unicorn.rotation(180)
    except NameError:
        print("could NOT find unicorn")
            

    while sc.SnakeIsAlive():
        pixelArray[sc.posX][sc.posY][1] = 255
        pixelArray[sc.posXPrev][sc.posYPrev][1] = 0

        sc.MoveSnake(1)

        if (sc.posX == apple.posX and sc.posY == apple.posY):
            DisplayApple(1)

        try:
            OutputFramework.setWindow(pixelArray)
        except NameError:
            DisplaySimulation()
        
        time.sleep(1)
        

    
    

if __name__ == "__main__":
        main()



    