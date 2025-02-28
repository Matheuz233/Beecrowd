while True:
    try:
        tempos = []

        for _ in range(int(input())):
            tempos.append(float(input()))

        print(min(tempos))

    except EOFError:
        break
