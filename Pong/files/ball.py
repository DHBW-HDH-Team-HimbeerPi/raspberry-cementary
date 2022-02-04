

class Ball:

    def __init__(self):
        self.xPosition = 7.0
        self.yPosition = 7.0
        self.size = 1
        self.r = 255
        self.g = 255
        self.b = 255
        self.verticalSpeed = 0.0
        self.speed = 0.2

    def move(self):
        self.xPosition = self.xPosition + self.speed
        self.yPosition = self.yPosition + self.verticalSpeed


    def bounce(self):
        self.verticalSpeed = -(self.verticalSpeed)

    def panelBounce(self, panel):
        self.speed = -(self.speed)
        if (panel.yPosition - self.yPosition) < 1:
            if self.verticalSpeed >= 0:
                self.verticalSpeed = self.verticalSpeed +  (1 * ((panel.yPosition - self.yPosition)/25))
            else:
                self.verticalSpeed = self.verticalSpeed * 1.005
        else:
            if self.verticalSpeed <= 0:
                self.verticalSpeed = self.verticalSpeed - (1 * ((panel.yPosition - self.yPosition)/25))
            else:
                self.verticalSpeed = self.verticalSpeed * 1.005

    @property
    def getCoordinate(self):
        return (self.xPosition, self.yPosition)