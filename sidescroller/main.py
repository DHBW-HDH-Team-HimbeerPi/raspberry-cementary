import time
import numpy as np
from src.shiftPixels import walkLeft, walkRight, shiftPixelsY
from src.addObject import add
from src.player import Player
from src.unicornHead import showUH
from src.spriteReader import dimensions
from src.sprites import Sprites
from src.directions import Directions
from src.sanitizePixelArray import sanatizeArray
from src.input import inputToDirection
try:
    from output_framework.output_framework import OutputFramework # type: ignore
    from input_framework.imu_controller import IMUController # type: ignore
    from input_framework.interface import ThresholdType, TriggerMode # type: ignore
except ImportError:
    print("no imports found")

PIXELS = 16
pixelArray = np.full((PIXELS, PIXELS*2, 4), 0)
pixelArray[10][10][0] = 255

def main():

    joe = Player()
    add(pixelArray, joe.dimensions(), False)
    add(pixelArray, dimensions(Sprites.mapStairs.value), True)
    add(pixelArray, dimensions(Sprites.mapPlatform.value), True)
    running = True
    try:
        rotationTreshold = 0.35
        controller = IMUController(TriggerMode.CALL_CHECK)
        controller.register_trigger(inputToDirection, {'dir' : Directions.up.value, 'pixelArray' : pixelArray}, controller.mov_x, rotationTreshold, ThresholdType.HIGHER)
        controller.register_trigger(inputToDirection, {'dir' : Directions.down.value, 'pixelArray' : pixelArray}, controller.mov_x, -rotationTreshold, ThresholdType.LOWER)
        controller.register_trigger(inputToDirection, {'dir' : Directions.left.value, 'pixelArray' : pixelArray}, controller.mov_y, -rotationTreshold, ThresholdType.LOWER)
        controller.register_trigger(inputToDirection, {'dir' : Directions.right.value, 'pixelArray' : pixelArray}, controller.mov_y, rotationTreshold, ThresholdType.HIGHER)
    except NameError:
        print("no controller found!")

    while running:
        try:
            OutputFramework.setWindow(sanatizeArray(pixelArray), 180)
            controller.check_triggers()
        except NameError:
            showUH(pixelArray, PIXELS)

if __name__ == "__main__":
    main()