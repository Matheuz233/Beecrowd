while True:
    try:
        h, m = map(int, input().split(":"))

        atraso = (8*60 - (h*60 + m)) - 60

        if atraso > 0:
            print(f"Atraso maximo: 0")
        else:
            print(f"Atraso maximo: {abs((8*60 - (h*60 + m)) - 60)}")
    except EOFError:
        break
