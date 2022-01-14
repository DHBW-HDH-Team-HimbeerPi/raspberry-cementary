def show(ausgabe: list):
    for x in range(len(ausgabe)):
        for y in range(len(ausgabe[0])):
            printed = False
            for color in range(len(ausgabe[0][0])):
                if(ausgabe[x][y][color] != 0):
                    print("0", end =" ")
                    printed = True
                    break
            if not printed:
                print("_", end =" ")
        print("")