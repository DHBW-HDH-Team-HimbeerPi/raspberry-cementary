import numpy as np
from src.addObject import add
from src.player import Player
from src.unicornHead import showUH
from src.directions import Directions
from src.sanitizePixelArray import sanatizeArray
from src.input import inputToDirection
from src.map import Map
try:
    from output_framework.output_framework import OutputFramework # type: ignore
    from input_framework.imu_controller import IMUController # type: ignore
    from input_framework.interface import ThresholdType, TriggerMode # type: ignore
except ImportError:
    print("no imports found")

PIXELS = 16
pixelArray = np.full((PIXELS, PIXELS*2, 4), 0)
pixelArray[0][0][0] = 255

def main():

    joe = Player(pixelArray)  # create Player
    map = Map()     # create Map
    
    print(joe.posX, joe.poxY)

    #add(pixelArray, dimensions(Sprites.mapStairs.value), True)
    running = True
    try:
        rotationTreshold = 0.35
        controller = IMUController(TriggerMode.CALL_CHECK)
        controller.register_trigger(inputToDirection, {'dir' : Directions.up.value, 'pixelArray' : pixelArray}, controller.mov_x, rotationTreshold, ThresholdType.HIGHER)
        controller.register_trigger(inputToDirection, {'dir' : Directions.down.value, 'pixelArray' : pixelArray}, controller.mov_x, -rotationTreshold, ThresholdType.LOWER)
        controller.register_trigger(inputToDirection, {'dir' : Directions.left.value, 'pixelArray' : pixelArray}, controller.mov_y, -rotationTreshold, ThresholdType.LOWER)
        controller.register_trigger(inputToDirection, {'dir' : Directions.right.value, 'pixelArray' : pixelArray}, controller.mov_y, rotationTreshold, ThresholdType.HIGHER)
    except NameError:
        print("No controller found!")

    while running:
        #map.updateMap(pixelArray, joe.posX)
        try:
            OutputFramework.setWindow(sanatizeArray(pixelArray), 180)
            controller.check_triggers()
        except NameError:
            showUH(pixelArray, PIXELS)

if __name__ == "__main__":
    main()