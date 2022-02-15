from enum import Enum
from .player import Player

class Directions(Enum):
    up = 1
    down = 2
    left = 3
    right = 4

def inputToDirection(dir, pixelArray, player: Player):
    if dir == Directions.right.value:
        player.walkRight()
    elif dir == Directions.left.value:
        player.walkLeft()
    elif dir == Directions.up.value:
        player.jump()
    else:
        print("down")
