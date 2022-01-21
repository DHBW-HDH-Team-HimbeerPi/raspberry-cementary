
        uh.clear()
        for i in range(0, PIXELS):
            for j in range(0, PIXELS):
                uh.set_pixel(i, j, pixelArray[i][j][0],  pixelArray[i][j][1],  pixelArray[i][j][2])
        uh.show()
        #OutputFramework.setWindow(pixelArray)
        time.sleep(0.5) 

if __name__ == "__main__":
    main()