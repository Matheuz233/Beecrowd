while True:
    try:
        v = float(input())
        d = float(input())
        r = d/2
        area = 3.14*r*r
        altura = v/(r*r*3.14)
        print(f"ALTURA = {altura:.2f}")
        print(f"AREA = {area:.2f}")

    except EOFError:
        break
