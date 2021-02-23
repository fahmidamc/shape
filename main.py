choice = ""
ch = ""
while True:
    print("_____PERIMETER AND AREA______")
    print("______________________________")
    print("1.PERIMETER")
    print("2.AREA")
    print("3.EXIT")
    choice = int(input("Select your choice"))
    if choice == 1:
        print("YOU SELECTED PERIMETER!!")
        print("---------SHAPES--------")
        print("1.CIRCLE")
        print("2.SQUARE")
        print("3.RECTANGLE")
        print("4.TRIANGLE")
        print("5.EXIT")

        ch = int(input("WHICH SHAPE DO YOU WANT"))
        if ch == 1:
            print("-----CIRCLE----")
            r = int(input("Enter circle's radius length: "))
            cir_perimeter = 2 * 3.14 * r
            print(f"The perimeter of circle is {circ_perimeter}.")

        elif ch == 2:
            print("-----SQUARE-------")
            side = int(input("Enter the side of square"))
            sq_perimeter = 4 * side
            print(f"The perimeter of square is {sq_perimeter}.")
        elif ch == 3:
            print("-----RECTANGLE-----")
            width = int(input("Enter the width of triangle"))
            length = int(input("Enter the length of triangle"))
            rec_perimeter = 2 * (width + length)
            print(f"The perimeter of rectangle is {rec_perimeter}.")

        elif ch == 4:
            print("-----TRIANGLE------")
            a = int(input("Enter length of first side"))
            b = int(input("Enter length of second side"))
            c = int(input("Enter length of third side"))
            tri_perimeter = a + b + c
            print(f"The perimeter of triangle is {tri_perimeter}.")

        elif ch == 5:
            print("program exiting...")

    if choice == 2:
        print("YOU SELECTED AREA!!")
        print("---------SHAPES--------")
        print("1.CIRCLE")
        print("2.SQUARE")
        print("3.RECTANGLE")
        print("4.TRIANGLE")
        print("5.EXIT")
        ch = int(input("WHICH SHAPE DO YOU WANT"))
        if ch == 1:
            print("-----CIRCLE-----")
            r = int(input("Enter circle's radius length: "))
            circ_area = 3.14 * r * r
            print(f"The area of triangle is {circ_area}.")
        if ch == 2:
            print("-----SQUARE------")
            s = int(input("Enter square's side length: "))
            sqt_area = s * s
            print(f"The area of square is {sqt_area}.")
        if ch == 3:
            print("------RECTANGLE-----")
            l = int(input("Enter rectangle's length: "))
            b = int(input("Enter rectangle's breadth: "))
            rect_area = l * b
            print(f"The area of rectangle is {rect_area}.")
        if ch == 4:
            print("------TRIANGLE------")
            h = int(input("Enter triangle's height length: "))
            b = int(input("Enter triangle's breadth length: "))
            tri_area = 0.5 * b * h
            print(f"The area of triangle is {tri_area}.")
        if ch == 5:
            print("program exiting...")
            print("program exiting...")
    if choice == 3:
        print("program exiting...")
