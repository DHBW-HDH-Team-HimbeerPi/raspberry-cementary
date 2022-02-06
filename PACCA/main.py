debug = 1
import csv
from pathlib import Path
import numpy as np
import time
import random
import pygame
from src.unicornHead import showUH
if debug != 1:
    from output_framework.output_framework import OutputFramework
import os
from pygame.locals import (

    K_UP,

    K_DOWN,

    K_LEFT,

    K_RIGHT,

    K_ESCAPE,

    KEYDOWN,

    QUIT,

)


# Initialize pygame

pygame.init()


def show(ausgabe: list):
    length = len(ausgabe)
    for y in range(length):
        for x in range(length):
            printed = False
            for color in range(3):
                if (ausgabe[x][y][color] == 91):
                    print("X", end=" ")
                    printed = True
                    break
                if (ausgabe[x][y][color] == 255):
                    print("1", end=" ")
                    printed = True
                    break
            if (not printed):
                print(" ", end=" ")
        print()


pixelArray = np.full((16, 16, 3), 0)
global lastdir
lastdir = 0
playerposition = [0, 0]
pixelArray[0][0][0] = 255
pixelArray[0][0][1] = 255


def createLevel():
    basePath = Path(__file__).parent
    filePath = (basePath / ("level.csv")).resolve()

    with open(filePath) as file:
        sprite = [line for line in csv.reader(file)]
    length = len(sprite)
    for y in range(length):
        for x in range(length):
            if (int(sprite[x][y]) == 1):
                pixelArray[x][y][0] = 91
                pixelArray[x][y][1] = 58
                pixelArray[x][y][2] = 41


def moveplayer(dira):
    global has_been_triggered
    global lastdir
   # if has_been_triggered != 0:
    #    return
    #else:
     #   has_been_triggered = 1
    dirb = dira
    moved = True
    for x in range(2):
        match dirb:
            case 1:
                if (playerposition[1] < 15 and pixelArray[playerposition[0]][playerposition[1] + 1][0] == 0):
                    pixelArray[playerposition[0]][playerposition[1] + 1][0] = 255
                    pixelArray[playerposition[0]][playerposition[1] + 1][1] = 255
                    pixelArray[playerposition[0]][playerposition[1]][0] = 0
                    pixelArray[playerposition[0]][playerposition[1]][1] = 0
                    playerposition[1] += 1
                    dirb = 0
                    if(x==1):
                        lastdir = dira
                else:
                    dirb = lastdir
            case 2:
                if (playerposition[1] > 0 and pixelArray[playerposition[0]][playerposition[1] - 1][0] == 0):
                    pixelArray[playerposition[0]][playerposition[1] - 1][0] = 255
                    pixelArray[playerposition[0]][playerposition[1] - 1][1] = 255
                    pixelArray[playerposition[0]][playerposition[1]][0] = 0
                    pixelArray[playerposition[0]][playerposition[1]][1] = 0
                    playerposition[1] -= 1
                    dirb = 0
                    if(x==1):
                        lastdir = dira
                else:
                    dirb = lastdir
            case 3:
                if (playerposition[0] < 15 and pixelArray[playerposition[0] + 1][playerposition[1]][0] == 0):
                    pixelArray[playerposition[0] + 1][playerposition[1]][0] = 255
                    pixelArray[playerposition[0] + 1][playerposition[1]][1] = 255
                    pixelArray[playerposition[0]][playerposition[1]][0] = 0
                    pixelArray[playerposition[0]][playerposition[1]][1] = 0
                    playerposition[0] += 1
                    dirb = 0
                    if(x==1):
                        lastdir = dira
                else:
                    dirb = lastdir
            case 4:
                if (playerposition[0] > 0 and pixelArray[playerposition[0] - 1][playerposition[1]][0] == 0):
                    pixelArray[playerposition[0] - 1][playerposition[1]][0] = 255
                    pixelArray[playerposition[0] - 1][playerposition[1]][1] = 255
                    pixelArray[playerposition[0]][playerposition[1]][0] = 0
                    pixelArray[playerposition[0]][playerposition[1]][1] = 0
                    playerposition[0] -= 1
                    dirb = 0
                    if(x==1):
                        lastdir = dira
                else:
                    dirb = lastdir
            case _:
                dirb = lastdir

def main():
    createLevel()
    show(pixelArray)     
    #ctrl = IMUController()
    #threshold  = 0.35
    #ctrl.register_trigger(moveplayer, {'dira' : 1 }, ctrl.mov_x, threshold, ThresholdType.HIGHER)
    #ctrl.register_trigger(moveplayer, {'dira' : 2 }, ctrl.mov_x, -threshold, ThresholdType.LOWER)
    #ctrl.register_trigger(moveplayer, {'dira' : 3 }, ctrl.mov_y, threshold, ThresholdType.HIGHER)
    #ctrl.register_trigger(moveplayer, {'dira' : 4 }, ctrl.mov_y, -threshold, ThresholdType.LOWER)
    #has_been_triggered = 0
    global lastdir 
    lastdir = 0
    for x in range(100):

        has_been_triggered = 0
        time.sleep(0.35)
        #ctrl.check_triggers()
        print(x)
        moved = False
        pressed_keys = pygame.key.get_pressed()  
        if pressed_keys[K_UP]:
            moveplayer(2)
            moved=True
        if pressed_keys[K_DOWN] and moved==False:
            moveplayer(1)
            moved=True
        if pressed_keys[K_RIGHT]and moved==False:
            moveplayer(3)
            moved=True
        if pressed_keys[K_LEFT] and moved==False:
            moveplayer(4)
            moved=True
        if moved==False:
            moveplayer(lastdir)

        showUH(pixelArray, 16)
        #else:
         #   OutputFramework.setWindow(pixelArray)
if __name__ == "__main__":
    main()