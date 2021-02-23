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
                r = int(input("Enter circle's radius length: "))
                circ_area = 3.14 * r * r
                print(f"The area of triangle is {circ_area}.")

            if ch == 2:
                print("chose square")
                s = int(input("Enter square's side length: "))
                sqt_area = s * s
                print(f"The area of square is {sqt_area}.")
            if ch == 3:
                print("chose rectangle")
                l = int(input("Enter rectangle's length: "))
                b = int(input("Enter rectangle's breadth: "))
                rect_area = l * b
                print(f"The area of rectangle is {rect_area}.")
            if ch == 4:
                print("choose triangle")
                h = int(input("Enter triangle's height length: "))
                b = int(input("Enter triangle's breadth length: "))
                tri_area = 0.5 * b * h
                print(f"The area of triangle is {tri_area}.")
            if ch == 5:
                print("program exiting...")
                print("program exiting...")

        if choice == 3:
            print("program exiting...")

