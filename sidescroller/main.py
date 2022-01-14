import os
import time
import numpy as np
from devShow import show
from shiftPixels import shiftPixels
from addObject import add
from player import Player
#from OutputFramework.OutFramework import OutputFramework as of

PIXELS = 16
pixelArray = np.full((PIXELS , PIXELS, 4), 0)
running = True
pixelArray[10][10][0] = 255

def main():

    joe = Player(PIXELS, 5, 255, 0, 0)
    while running:
        #events
            #input
        #update
        add(pixelArray, joe.dimensions())
        shiftPixels(pixelArray)
        #draw
        show(pixelArray)
        time.sleep(2) 
        os.system('cls')

if __name__ == "__main__":
    main()
        





