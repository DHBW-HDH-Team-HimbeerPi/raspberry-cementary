import time
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


def main():

    gameRunning = True
    CreateGamefield()
    pixelArray[apple.AppleSpawner(sc)[0]][apple.AppleSpawner(sc)[1]][0] = 255

    #unicorn.rotation(180)

    while sc.SnakeIsAlive():
        pixelArray[sc.posX][sc.posY][1] = 255
        pixelArray[sc.posXOld][sc.posYOld][1] = 0

        sc.MoveSnake(1)

        if (sc.posX == apple.posX and sc.posY == apple.posY):
            pixelArray[apple.AppleSpawner(sc)[0]][apple.AppleSpawner(sc)[1]][0] = 255

        #DisplaySimulation()
        OutputFramework.setWindow(pixelArray)
        time.sleep(1)
        

    
    

if __name__ == "__main__":
        main()



    