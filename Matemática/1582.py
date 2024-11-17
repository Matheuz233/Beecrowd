while True:
    try:
        x, y, z = map(int, input().split())

        if x > y:
            x, y = y, x
        if y > z:
            y, z = z, y
        if x > y:
            x, y = y, x

        if x**2 + y**2 == z**2:
            a, b, c = x, y, z
            while b != 0:
                a, b = b, a % b
            mdc_xy = a

            a, b = mdc_xy, z
            while b != 0:
                a, b = b, a % b
            mdc_xyz = a

            if mdc_xyz == 1:
                print("tripla pitagorica primitiva")
            else:
                print("tripla pitagorica")
        else:
            print("tripla")
    except EOFError:
        break
