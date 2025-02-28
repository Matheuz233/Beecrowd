for _ in range(int(input())):
    t = int(input())

    resultado = str(t/2).split('.')

    if int(resultado[1]) > 0:
        print(int(resultado[0]) + 1)
    else:
        print(int(resultado[0]))
