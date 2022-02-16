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
#from src.unicornHead import showUH
from output_framework.output_framework import OutputFramework
import os
from input_framework.imu_controller import IMUController
from input_framework.interface import ThresholdType, TriggerMode



# Initialize pygame



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
    if has_been_triggered != 0:
        return
    else:
       has_been_triggered = 1
   
    moved = True
    
    if(dira==1):
        Joe.move(1,pixelArray)
    else:
        if(dira==2):
            Joe.move(2,pixelArray)
        else:
            if(dira==3):
                Joe.move(3,pixelArray)
            else:
                if(dira==4):    
                    Joe.move(4,pixelArray)
                else:
                    Joe.move(0,pixelArray)
def main():
    #pygame.init()
    global has_been_triggered
    global pixelArray
    pixelArray = np.full((16, 16, 3), 0)
    lastdir = 0
    pixelArray[0][0][0] = 255
    pixelArray[0][0][1] = 255
    pixelArray[15][15][2] = 255
    pixelArray[15][15][1] = 255
    pixelArray = lm.createLevel(pixelArray,2)
    ctrl = IMUController()
    threshold  = 0.35
    ctrl.register_trigger(moveplayer, {'dira' : 3 }, ctrl.mov_x, threshold, ThresholdType.HIGHER)
    ctrl.register_trigger(moveplayer, {'dira' : 4 }, ctrl.mov_x, -threshold, ThresholdType.LOWER)
    ctrl.register_trigger(moveplayer, {'dira' : 2 }, ctrl.mov_y, threshold, ThresholdType.HIGHER)
    ctrl.register_trigger(moveplayer, {'dira' : 1 }, ctrl.mov_y, -threshold, ThresholdType.LOWER)
    has_been_triggered = False
    global moved
    global Joe
    global EMEMIES

    ENEMIES = []
    mama = Enemy(15,15)
    score =0
    dada = Enemy(15,0)
    coin = Coin(pixelArray)
    papa = Enemy(0,15)
    ENEMIES.append(mama)
    ENEMIES.append(papa)
    ENEMIES.append(dada)
    Joe = Player(0,0)
    lastdir = 0
    x = 0
    while (lm.checkalive(Joe,ENEMIES)==True):

        if ( debug==1):         
            has_been_triggered = 0
            time.sleep(0.35)
            ctrl.check_triggers()
            moveplayer(0)
            print(score)
            moved = False
            """pressed_keys = pygame.key.get_pressed()  
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
                moveplayer(lastdir) """
            if(lm.checkcoin(Joe,coin)==True):
                score+=1
                pixelArray[coin.posxy[0]][coin.posxy[1]][2]=0
                coin = Coin(pixelArray)
            coin.showcoin(pixelArray)
            if (x%8!=0):
                for obj in ENEMIES:
                    obj.move(Joe.posxy,pixelArray)
            #showUH(pixelArray, 16)
            x+=1
            OutputFramework.setWindow(pixelArray)
if __name__ == "__main__":
    main()