from enum import Enum
from .map import Map
from .frameBuffer import FrameBuffer
from .player import Player

class Directions(Enum):
    left = 1
    right = 2
    down = 3
    up = 4

def inputToDirection(dir, pixelArray, player: Player, frameBuffer: FrameBuffer, map: Map):
    print(dir)
    if dir == Directions.right.value:
        if player.posY < 7:
            player.walkRight(pixelArray)
        else:
            map.moveCameraY()

    elif dir == Directions.left.value:
        player.walkLeft(pixelArray)

    elif dir == Directions.up.value:
        player.jump(pixelArray, frameBuffer)
