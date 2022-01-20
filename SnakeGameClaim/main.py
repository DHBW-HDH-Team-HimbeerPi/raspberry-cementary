import numpy as np
import random
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
    
    applePosX = random.randrange(1, 14)
    applePosY = random.randrange(1, 14)

    while(applePosX != SnakeController.posX and applePosY != SnakeController.posY):
        applePosX = random.randrange(1, 14)
        applePosY = random.randrange(1, 14)
    
    pixelArray[applePosX][applePosY][0] = 255


def main():

    CreateGamefield()
    AppleSpawner()

    while gameRunning:
        #code
        gameRunning = False

    
    if __name__ == "__main__":
        main()





    