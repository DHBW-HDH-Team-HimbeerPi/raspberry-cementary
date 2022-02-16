
        controller.register_trigger(inputToDirection, { 'dir' : 1, 'pixelArray': pixelArray, 'player' : player, 'frameBuffer': frameBuffer }, controller.mov_x, rotationTreshold, ThresholdType.HIGHER)
        controller.register_trigger(inputToDirection, { 'dir' : 2, 'pixelArray': pixelArray, 'player' : player, 'frameBuffer': frameBuffer }, controller.mov_x, -rotationTreshold, ThresholdType.LOWER)
        controller.register_trigger(inputToDirection, { 'dir' : 3, 'pixelArray': pixelArray, 'player' : player, 'frameBuffer': frameBuffer }, controller.mov_y, -rotationTreshold, ThresholdType.LOWER)
        controller.register_trigger(inputToDirection, { 'dir' : 4, 'pixelArray': pixelArray, 'player' : player, 'frameBuffer': frameBuffer }, controller.mov_y, rotationTreshold, ThresholdType.HIGHER)
    except NameError:
        print("No controller found!")

    frames = 0

    while running:
        frames += 1
        bufferRunning = False

        if frameBuffer.length() > 0:
            bufferRunning = True
            frameBuffer.nextFrame(pixelArray)

        #print(player.posX, player.posY)
        try:
            OutputFramework.setWindow(sanatizeArray(pixelArray), 180)
            if not bufferRunning and not player.isJumping:
                controller.check_triggers()
        except NameError:
            showUH(pixelArray, PIXELS)
                
        #if frames % 8 == 0:
            #map.moveCameraY()
        
        player.shiftPlayerDown(pixelArray)

        time.sleep(1/2)
                

if __name__ == "__main__":
    main()