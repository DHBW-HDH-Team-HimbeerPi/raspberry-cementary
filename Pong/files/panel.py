

class Panel:
    def __init__(self, x: int, r: int, g: int, b: int):
        self.size = 4
        self.xPosition = x
        self.yPosition = 6.0
        self.r = r
        self.g = g
        self.b = b

    def moveUp(self):
        if self.yPosition > 0:
            self.yPosition = self.yPosition - 0.3

    def moveDown(self):
        if self.yPosition + 4 < 16:
            self.yPosition = self.yPosition + 0.3


    @property
    def getCoordinate(self):
        return (self.xPosition, self.yPosition)