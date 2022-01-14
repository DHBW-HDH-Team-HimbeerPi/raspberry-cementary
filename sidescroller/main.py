import os
import time
import numpy as np
from devShow import show
from shiftPixels import shiftPixels
from addObject import add
from player import Player
from output_framework.output_framework import OutputFramework

PIXELS = 16
pixelArray = np.full((PIXELS , PIXELS, 4), 0)
running = True
pixelArray[10][10][0] = 255

def main():

    joe = Player(PIXELS)
    add(pixelArray, joe.dimensions())
    #show(pixelArray)

    while running:
        #events
            #input
        #update
        shiftPixels(pixelArray)
        #draw
        #show(pixelArray)
        OutputFramework.setWindow(pixelArray)
        time.sleep(0.5) 
        #os.system('cls')

if __name__ == "__main__":
    main()
        





