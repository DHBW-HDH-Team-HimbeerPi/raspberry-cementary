import numpy as np
#from OutputFramework.OutFramework import OutputFramework as of

print("hello")

def show(ausgabe: list):
    length = len(ausgabe)
    for x in range(length):
        for y in range(length):
            printed = 0
            for color in range(3):
                if(ausgabe[x][y][color] != 0):
                    print("0", end =" ")
                    break
                else:
                    if (printed == 0):
                        print("_", end =" ")
                        printed = 1
        print("")

pixels = 3
pixelArray = np.full((pixels , pixels, 3), 0)

pixelArray[1][1][0] = 3

show(pixelArray)



            
                




#show(pixelArray)



