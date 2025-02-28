while True:
    try:
        N, R = map(int, input().split(" "))
        voluntarios = list(map(int, input().split(" ")))
        naoVoltaram = list(range(1, N + 1))
        for x in voluntarios:
            if x in voluntarios:
                naoVoltaram.pop(naoVoltaram.index(x))
        if len(naoVoltaram) == 0:
            print("*")
        else:
            for y in naoVoltaram:
                print(f'{y} ', end='')
            print()
    except EOFError:
        break