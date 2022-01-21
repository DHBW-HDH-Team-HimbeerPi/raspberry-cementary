import csv

import numpy


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
        print("test")
def createLevel():
    basePath = Path(__file__)
    filePath = (basePath / ("level").resolve())

    with open(filePath) as file:
        sprite = [line for line in csv.reader(file)]
    length = len(sprite)
    for y in range(length):
        for x in range(length):
            if(sprite[x][y]!=0):
                pixelArray[x][y][0] = 255
def main():
    pixelArray = np.full((16 , 16, 3), 0)
    show(pixelArray)

