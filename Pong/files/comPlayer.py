

class aiPlayer:

    def play(self, yBall, yPanel):
        if yBall > yPanel and yBall < yPanel :
            return 0
        else:
            if yBall < yPanel +1:
                return 1
            else:
                if yBall > yPanel+2:
                    return -1
        return 0