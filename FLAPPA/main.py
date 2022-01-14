import numpy as np
import time
import random
import os

from output_framework.output_framework 
import OutputFramework as oF


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
    return False
def movewall(pixelArray,wallocation):
    for walls in range (3):
        if (walllocation[walls] == 0):
            walllocation[walls]= 36
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
    while i <r :
        pixelArray[15][i][1]=255
        i+=1
    i=15
    while i>r+4:
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

pixelArray = np.full((16 , 16, 3), 0)
walllocation = [16,28,4]
pixelArray[3][8][0] = 250

for u in range (60):
    movewall(pixelArray,walllocation)
    time.sleep(0.1)
    os.system('cls')
    OutputFramework.setWindow(pixelArray)
    #show(pixelArray)
    if (checkalive(pixelArray)==False):
        break
