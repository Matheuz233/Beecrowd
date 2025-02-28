for _ in range(int(input())):
    int(input())

    M = list(map(int, input().split()))

    impares = []

    for i in M:
        if i % 2 != 0:
            impares.append(i)

    impares.sort()

    resultado = []

    while impares:
        if impares:
            resultado.append(impares.pop())
        if impares:
            resultado.append(impares.pop(0))

    print(" ".join(map(str, resultado)))
