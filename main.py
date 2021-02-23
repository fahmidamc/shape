choice =""
ch =""
while True:
    print("_____PERIMETER AND AREA______")
    print("______________________________")
    print("1.PERIMETER")
    print("2.AREA")
    print("3.EXIT")
    choice = int(input("select your choice"))
    if choice == 1:
        print("YOU SELECTED PERIMETER!!")
        print("---------SHAPES--------")
        print("1.CIRCLE")
        print("2.SQUARE")
        print("3.RECTANGLE")
        print("4.TRIANGLE")
        print("5.EXIT")
        while True:
            ch = int(input("WHICH SHAPE DO YOU WANT"))
            if ch == 1:
                print("chose circle")
            elif ch == 2:
                print("chose square")
            elif ch == 3:
                print("chose rectangle")
            elif ch == 4:
                print("choose triangle")

            elif ch == 5:
                print("program exiting...")
                break
    if choice == 2:
            print("YOU SELECTED AREA!!")
            print("---------SHAPES--------")
            print("1.CIRCLE")
            print("2.SQUARE")
            print("3.RECTANGLE")
            print("4.TRIANGLE")
            print("5.EXIT")
            ch = int(input("WHICH SHAPE DO YOU WANT"))
            if ch == 2:
                print("chose circle")
            if ch == 2:
                print("chose square")
            if ch == 3:
                print("chose rectangle")
            if ch == 4:
                print("choose triangle")
            if ch == 5:
                print("program exiting...")

        if choice == 3:
            print("program exiting...")

