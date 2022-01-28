from .directions import Directions
from src.shiftPixels import shiftPlayerDown, shiftPlayerUp, walkRight, walkLeft

def inputToDirection(dir, pixelArray):
    if(dir == Directions.up.value):
        shiftPlayerDown(pixelArray)
    elif(dir == Directions.down.value):
        shiftPlayerUp(pixelArray)
    elif(dir == Directions.left.value):
        walkLeft(pixelArray)
    else:
        walkRight(pixelArray)
