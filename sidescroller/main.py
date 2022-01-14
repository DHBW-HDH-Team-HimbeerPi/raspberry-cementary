import os
import time
import numpy as np
from devShow import show
from shiftPixels import shiftPixels
from player import Player
#from OutputFramework.OutFramework import OutputFramework as of

PIXELS = 16
pixelArray = np.full((PIXELS , PIXELS, 3), 0)
running = True
pixelArray[10][10][0] = 255

def main():

    joe = Player(PIXELS, 3, 255, 0, 0)
    while running:
        #events
        #update
        shiftPixels(pixelArray)
        #draw
        show(pixelArray)
        time.sleep(2) 
        os.system('cls')

if __name__ == "__main__":
    main()
        





