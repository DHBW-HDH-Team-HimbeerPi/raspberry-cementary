import time
import numpy as np
from src.shiftPixels import shiftPlayerDown, shiftPlayerUp, shiftPixelsY
from src.addObject import add
from src.player import Player
from src.unicornHead import showUH
from src.spriteReader import dimensions
from src.sprites import Sprites
#from output_framework.output_framework import OutputFramework

PIXELS = 16
pixelArray = np.full((PIXELS, PIXELS*2, 4), 0)
pixelArray[10][10][0] = 255

def main():

    joe = Player()
    add(pixelArray, joe.dimensions(), False)
    add(pixelArray, dimensions(Sprites.map1.value), True)
    #show(pixelArray)
    running = True
    times = 0

    while running:
        if(times == 10):
            add(pixelArray, dimensions(Sprites.map1.value), True)
        #events
        #input
        #update
        showUH(pixelArray, PIXELS)
        running = shiftPixelsY(pixelArray)
        #draw
        #OutputFramework.setWindow(pixelArray)
        times = times+1
        time.sleep(0.5) 

if __name__ == "__main__":
    main()
        





