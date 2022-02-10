from enum import Enum

class Sprites(Enum):
    player = "amogus.csv"
    mapStairs = "stairs.csv"
    mapPlatformHigh = "platformHigh.csv"
    mapPlatformLow = "platformLow.csv"

def numberToSprite(spriteNumber):
        if spriteNumber == 1:
            return Sprites.mapStairs.value
        elif spriteNumber == 2:
            return Sprites.mapPlatformHigh.value
        elif spriteNumber == 3:
            return Sprites.mapPlatformLow.value
        else:
            return None