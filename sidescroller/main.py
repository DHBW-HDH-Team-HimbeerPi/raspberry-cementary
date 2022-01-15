import os
import time
import numpy as np
from src.devShow import show
from src.shiftPixels import shiftPixels
from src.addObject import add
from src.player import Player
#from output_framework.output_framework import OutputFramework

PIXELS = 16
pixelArray = np.full((PIXELS , PIXELS, 4), 0)
pixelArray[10][10][0] = 255

def main():

    joe = Player(PIXELS)
    add(pixelArray, joe.dimensions())
    #show(pixelArray)
    running = True

    while running:
        #events
            #input
        #update
        running = shiftPixels(pixelArray)
        #draw
        show(pixelArray)
        #OutputFramework.setWindow(pixelArray)
        time.sleep(5) 
        #os.system('cls')

if __name__ == "__main__":
    main()
        





