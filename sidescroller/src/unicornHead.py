from unicorn_hat_sim import unicornhathd as uh

def showUH(pixelArray: list, pixels):
    uh.rotation(270)
    uh.clear()
    for i in range(0, pixels):
        for j in range(0, pixels):
            uh.set_pixel(i, j, pixelArray[i][j][0],  pixelArray[i][j][1],  pixelArray[i][j][2])
    uh.show()