try:
    from unicorn_hat_sim import unicornhathd as uh
except ImportError:
    print("no uh sim!")

def showUH(pixelArray: list, pixels):
    uh.rotation(0)
    uh.clear()
    for i in range(0, pixels):
        for j in range(0, pixels):
            uh.set_pixel(15-i,j, pixelArray[i][j][0],  pixelArray[i][j][1],  pixelArray[i][j][2])
    uh.show()