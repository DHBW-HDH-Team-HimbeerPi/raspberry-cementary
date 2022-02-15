debug = 1
import csv
from src.player import Player
from src.ghost import Enemy
from src.coin import Coin
import src.levelmanager as lm
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
pixelArray[0][0][0] = 255
pixelArray[0][0][1] = 255
pixelArray[15][15][2] = 255
pixelArray[15][15][1] = 255

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
    global Joe
   # if has_been_triggered != 0:
    #    return
    #else:
     #   has_been_triggered = 1
   
    moved = True
    
    match dira:
        case 1:
            Joe.move(1,pixelArray)
        case 2:
            Joe.move(2,pixelArray)
        case 3:
            Joe.move(3,pixelArray)
        case 4:
            Joe.move(4,pixelArray)
        case _:
            Joe.move(0,pixelArray)

def main():
    global pixelArray
    pixelArray = lm.createLevel(pixelArray,3)
    show(pixelArray)     
    #ctrl = IMUController()
    #threshold  = 0.35
    #ctrl.register_trigger(moveplayer, {'dira' : 1 }, ctrl.mov_x, threshold, ThresholdType.HIGHER)
    #ctrl.register_trigger(moveplayer, {'dira' : 2 }, ctrl.mov_x, -threshold, ThresholdType.LOWER)
    #ctrl.register_trigger(moveplayer, {'dira' : 3 }, ctrl.mov_y, threshold, ThresholdType.HIGHER)
    #ctrl.register_trigger(moveplayer, {'dira' : 4 }, ctrl.mov_y, -threshold, ThresholdType.LOWER)
    #has_been_triggered = 0
    global lastdir 
    global moved
    global Joe
    global EMEMIES
    ENEMIES = []
    mama = Enemy(15,15)
    dada = Enemy(15,0)
    coin = Coin(pixelArray)
    papa = Enemy(0,15)
    ENEMIES.append(mama)
    ENEMIES.append(papa)
    ENEMIES.append(dada)
    Joe = Player(0,0)
    lastdir = 0
    for x in range(100):
        has_been_triggered = 0
        time.sleep(0.2)
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
        if(lm.checkCoin(coin)==True):
            pixelArray[coin.posxy[0]][coin.posxy[1]][2]=0
            coin = Coin(pixelArray)
        coin.showCoin(pixelArray)
        if (x%3!=0):
            for obj in ENEMIES:
                obj.move(Joe.posxy,pixelArray)
        showUH(pixelArray, 16)
        if(lm.checkalive(Joe,ENEMIES) == False):
            break
        #else:
         #   OutputFramework.setWindow(pixelArray)
if __name__ == "__main__":
    main()