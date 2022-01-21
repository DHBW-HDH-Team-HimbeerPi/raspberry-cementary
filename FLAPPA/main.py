import numpy as np
import time
import random
import math
import os
from input_framework.imu_controller import IMUController
from input_framework.interface import ThresholdType, TriggerMode


from output_framework.output_framework import OutputFramework 


def show(ausgabe: list):
    length = len(ausgabe)
    for y in range(length):
        for x in range(length):
            printed = False
            for color in range(3):
                if(ausgabe[x][y][color] == 255):
                    print("0", end =" ")
                    printed = True
                    break
                if(ausgabe[x][y][color] == 250):
                    print("1", end =" ")
                    printed = True
                    break
            if (not printed):
                print("_", end =" ")
        print("")
def checkalive(pixelArray):
    for y in range (15):
        if(pixelArray[3][y][0]!=0):
            return True
    # eigenlich false
    return False






def playermovement(velocity):
    pixelArray[3][subposition][0] = 0
    subposition+=velocity*0.5
    if (subposition > 15 ):
        subposition =15
    if (subposition < 0 ):
        subposition = 0
    pixelArray[3][subposition][0] = 250


def movewall(pixelArray,wallocation):
    for walls in range (3):
        if (walllocation[walls] == 0):
            walllocation[walls]= 36
            walllocation[3]=walllocation[3] + 1
            print(walllocation[3])
            movewallleft(pixelArray,0)
            
        elif(walllocation[walls] == 16):
            createwall(pixelArray)
            walllocation[walls] =15
        elif(walllocation[walls]<16):
            movewallleft(pixelArray,walllocation[walls])
            walllocation[walls]-=1
        else:
            walllocation[walls]-=1
def createwall(pixelArray):
    r = random.randrange(11)
    i=0
    
    if walllocation[3]>10:
        difficulty = 2
    else:
        difficulty = 3
    print (difficulty)
    print(walllocation[3])
    while i <r :
        pixelArray[15][i][1]=255
        i+=1
    i=15
    while i>r+difficulty:
        pixelArray[15][i][1]=255
        i-=1
def movewallleft(pixelArray,wall):
    for y in range(16):
        if (pixelArray[wall][y][1]!=0):
            movepixelleft(pixelArray,wall,y)

def movepixelleft(ausgabe,x,y):
    for color in range(3):
        if (x!=0):
            ausgabe[x-1][y][color] = ausgabe[x][y][color]   
        ausgabe[x][y][color] = 0;


ctrl = IMUController(TriggerMode.CALL_CHECK)
ctrl.register_trigger(playermovement, {'velocity' : 0.4 }, ctrl.mov_y, 2, ThresholdType.HIGHER)
ctrl.register_trigger(playermovement, {'velocity' : 0.6 }, ctrl.mov_y, 3, ThresholdType.HIGHER)
pixelArray = np.full((16 , 16, 3), 0)
walllocation = [16,28,40,0]
pixelArray[3][8][0] = 250
for u in range (240):
    playersubposition = 8
    movewall(pixelArray,walllocation)
    time.sleep(0.1/math.log(walllocation[3]+2,15))
    #os.system('cls')
    ctrl.check_triggers()
    OutputFramework.setWindow(pixelArray)
    #show(pixelArray)
    if (checkalive(pixelArray)==False):
        break

