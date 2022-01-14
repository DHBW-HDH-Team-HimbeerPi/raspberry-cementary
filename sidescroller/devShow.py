class DevShow:

    def show(self, ausgabe: list):
        length = len(ausgabe)
        for x in range(length):
            for y in range(length):
                printed = False
                for color in range(3):
                    if(ausgabe[x][y][color] != 0):
                        print("0", end =" ")
                        printed = True
                        break
                if (not printed):
                    print("_", end =" ")
            print("")
