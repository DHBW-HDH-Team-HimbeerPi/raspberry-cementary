import numpy as np
from devShow import DevShow
#from OutputFramework.OutFramework import OutputFramework as of

dev = DevShow()

PIXELS = 16
pixelArray = np.full((PIXELS , PIXELS, 3), 0)

pixelArray[1][1][0] = 255

dev.show(pixelArray)



