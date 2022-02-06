import numpy as np
import time
import random
import math
import os
#from input_framework.imu_controller import IMUController
#from input_framework.interface import ThresholdType, TriggerMode
global difficulty
global playerposition
global score
#from output_framework.output_framework import OutputFramework 


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
    global playerposition
    for x in range (3):
        if(walllocation[x]==3 ): 
            for y in range (15):
                    if(playerposition>walllocation[x*2+3] and playerposition<walllocation[x*2+4]):
                        return True
                    else:
                        return False
            return True



def playermovement(velocity):
    global pixelArray
    global playerposition
    pixelArray[3][playerposition][0] = 0
    playerposition+=velocity
    if (playerposition > 15 ):
        playerposition=0
    if (playerposition < 0 ):
        playerposition=15;
    pixelArray[3][playerposition][0] = 250


def movewall(pixelArray,walllocation):
    global score
    for walls in range (3):
        if (walllocation[walls] == 0):
            walllocation[walls]= 36
            score=score + 1
            print(score)
            movewallleft(pixelArray,0)
            
        elif(walllocation[walls] == 16):
            createwall(pixelArray,walls)
            walllocation[walls] =15
        elif(walllocation[walls]<16):
            movewallleft(pixelArray,walllocation[walls])
            walllocation[walls]-=1
        else:
            walllocation[walls]-=1
def createwall(pixelArray,walls):
    global score
    r = random.randrange(11)
    i=0
    global difficulty   
    if score>10:
        difficulty = 2
    else:
        difficulty = 3
    print (difficulty)
    print(score)
    walllocation[walls*2+3]=-1
    while i <r :
        pixelArray[15][i][1]=255
        i+=1
        walllocation[walls*2+3]=i
    i=15
    walllocation[walls*2+4]=-1
    while i>r+difficulty:
        pixelArray[15][i][1]=255
        i-=1
        walllocation[walls*2+4]=i
def movewallleft(pixelArray,wall):
    for y in range(16):
        if (pixelArray[wall][y][1]!=0):
            movepixelleft(pixelArray,wall,y)

def movepixelleft(ausgabe,x,y):
    for color in range(3):
        if (x!=0):
            ausgabe[x-1][y][color] = ausgabe[x][y][color]   
        ausgabe[x][y][color] = 0;

def main():
   # ctrl = IMUController(TriggerMode.CALL_CHECK)
    #ctrl.register_trigger(playermovement, {'velocity' : 1 }, ctrl.mov_x, 0.35, ThresholdType.HIGHER)
    #ctrl.register_trigger(playermovement, {'velocity' : -1 }, ctrl.mov_x, -0.35, ThresholdType.LOWER)
    global pixelArray
    pixelArray = np.full((16 , 16, 3), 0)
    global walllocation
    walllocation = [16,28,40,0,0,0,0,0,0]

    global playerposition
    global score
    score =0;
    playerposition = 8
    pixelArray[3][8][0] = 250
    for u in range (240):

        movewall(pixelArray,walllocation)
    #    OutputFramework.setWindow(pixelArray)
     #
     # 
     # 
     # 
     #    ctrl.check_triggers()
        time.sleep(0.1/math.log(score+2,15)/8)
        if (checkalive(pixelArray)==False):
            break
       # OutputFramework.setWindow(pixelArray)
        #ctrl.check_triggers()
        if (checkalive(pixelArray)==False):
            break
        #OutputFramework.setWindow(pixelArray)
        #ctrl.check_triggers()
        time.sleep(0.1/math.log(score+2,15)/8)
        #OutputFramework.setWindow(pixelArray)
        #show(pixelArray)
        if (checkalive(pixelArray)==False):
            break

if __name__ == "__main__":
    main()