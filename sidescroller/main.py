import time
import numpy as np
from src.shiftPixels import shiftPlayerDown, shiftPlayerUp, shiftPixelsY
from src.addObject import add
from src.player import Player
from src.unicornHead import showUH
#from output_framework.output_framework import OutputFramework

PIXELS = 16
pixelArray = np.full((PIXELS*2 , PIXELS, 4), 0)
#pixelArray[10][10][0] = 255

def main():

    joe = Player()
    add(pixelArray, joe.dimensions(), PIXELS)
    #show(pixelArray)
    running = True

    while running:
        #events
        #input
        #update
        showUH(pixelArray, PIXELS)
        running = shiftPixelsY(pixelArray)
        shiftPlayerUp(pixelArray)
        #draw
        #OutputFramework.setWindow(pixelArray)
        time.sleep(0.5) 

if __name__ == "__main__":
    main()
        





