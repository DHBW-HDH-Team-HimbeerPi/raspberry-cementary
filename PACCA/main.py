import csv
from pathlib import Path
import numpy as np


def show(ausgabe: list):
    length = len(ausgabe)
    for y in range(length):
        for x in range(length):
            printed = False
            for color in range(3):
                if(ausgabe[x][y][color] == 91):
                    print("0", end =" ")
                    printed = True
                    break
                if(ausgabe[x][y][color] == 250):
                    print("1", end =" ")
                    printed = True
                    break
            if (not printed):
                print("/", end =" ")
        print()
def movepixelleft(ausgabe,x,y):
    for color in range(3):
        if (x!=0):
            ausgabe[x-1][y][color] = ausgabe[x][y][color]   
        ausgabe[x][y][color] = 0;

pixelArray = np.full((16 , 16, 3), 0)
walllocation = [16,28,40,0]
pixelArray[3][8][0] = 250

def createLevel():
    basePath = Path(__file__).parent
    filePath = (basePath / ("level.csv")).resolve()

    with open(filePath) as file:
        sprite = [line for line in csv.reader(file)]
    length = len(sprite)
    for y in range(length):
        for x in range(length):
            if(int(sprite[x][y])==1):
                pixelArray[x][y][0] = 91
                pixelArray[x][y][1] = 58
                pixelArray[x][y][2] = 41
pixelArray = np.full((16 , 16, 3), 0)
show(pixelArray)
createLevel()
show(pixelArray)
