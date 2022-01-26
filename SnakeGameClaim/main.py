import time
import numpy as np
import random
try:
    from output_framework.output_framework import OutputFramework 
    from input_framework.imu_controller import IMUController
    from input_framework.interface import ThresholdType, TriggerMode
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
sleepTime = 0.5

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

def SnakeAutoPilot():
    if(apple.posY != sc.posY[0]):
        if (apple.posY > sc.posY[0]):
            sc.MoveSnake(1)
        else:
            sc. MoveSnake(2)
    elif(apple.posX != sc.posX[0]):
        if (apple.posX > sc.posX[0]):
            sc.MoveSnake(4)
        else:
            sc.MoveSnake(3)        

def main():
    rotationTreshhold = 1.5

    controller = IMUController(TriggerMode.CALL_CHECK)
    controller.register_trigger(sc.MoveSnake, {'direction' : 1}, controller.rot_x, rotationTreshhold, ThresholdType.HIGHER)
    controller.register_trigger(sc.MoveSnake, {'direction' : 2}, controller.rot_x, rotationTreshhold, ThresholdType.LOWER)
    controller.register_trigger(sc.MoveSnake, {'direction' : 3}, controller.rot_y, rotationTreshhold, ThresholdType.HIGHER)
    controller.register_trigger(sc.MoveSnake, {'direction' : 4}, controller.rot_y, rotationTreshhold, ThresholdType.LOWER)

    gameRunning = True
    sleepTime = 0.5
    CreateGamefield()
    DisplayApple(0)

    
    try:
        unicorn.rotation(180)
    except NameError:
        print("could NOT find unicorn")
            

    while sc.SnakeIsAlive():
        pixelArray[sc.posXPrev][sc.posYPrev][1] = 0

        if (sc.posX[0] == apple.posX and sc.posY[0] == apple.posY):
            sc.EatApple()
            DisplayApple(1)

            if (len(sc.posX) >= 3 and sleepTime > 0.1):
                sleepTime -= 0.025

        for i in range(0, len(sc.posX)):
            pixelArray[sc.posX[i]][sc.posY[i]][1] = 255
            
        #sc.MoveSnake(4)
        #SnakeAutoPilot()

        controller.check_triggers()

        try:
            OutputFramework.setWindow(pixelArray)
        except NameError:
            DisplaySimulation()
        
        time.sleep(sleepTime)
        

    
    

if __name__ == "__main__":
    main()



    