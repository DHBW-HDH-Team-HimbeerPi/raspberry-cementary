from directions import Directions
from src.shiftPixels import shiftPlayerDown, shiftPlayerUp, shiftPixelsY

def inputToDirection(dir, pixelArray):
    if(dir == Directions.up.value):
        shiftPlayerDown(pixelArray)
    elif(dir == Directions.down.value):
        shiftPlayerUp(pixelArray)
    elif(dir == Directions.left.value):
        shiftPixelsY
    else:
        print("bruh")
