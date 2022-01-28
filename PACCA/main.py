debug = 0
import csv
from pathlib import Path
import numpy as np
import time
import random

if debug != 1:
    from output_framework.output_framework import OutputFramework
import os


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
    if has_been_triggered != 0:
        return
    else:
        has_been_triggered = 1
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
                    lastdir = dira
                else:
                    dirb = lastdir
            case _:
                dirb = lastdir

createLevel()
show(pixelArray)
if debug == 1:
    os.system('cls')

ctrl = IMUController()
threshold = 0.35
ctrl.register_trigger(moveplayer, {'dira' : 1 }, ctrl.mov_x, threshold, ThresholdType.HIGHER)
ctrl.register_trigger(moveplayer, {'dira' : 2 }, ctrl.mov_x, -threshold, ThresholdType.LOWER)
ctrl.register_trigger(moveplayer, {'dira' : 3 }, ctrl.mov_y, threshold, ThresholdType.HIGHER)
ctrl.register_trigger(moveplayer, {'dira' : 4 }, ctrl.mov_y, -threshold, ThresholdType.LOWER)
has_been_triggered = 0

for x in range(100):

    has_been_triggered = 0
    time.sleep(0.4)
    ctrl.check_triggers()
    if debug == 1:
        moveplayer(random.randrange(4) + 1)
        os.system('cls')
        show(pixelArray)
    else:
        OutputFramework.setWindow(pixelArray)
