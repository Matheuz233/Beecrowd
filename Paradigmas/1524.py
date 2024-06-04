while True:
    try:
        Nint, K = map(int, input().split())
        N = list(map(int, input().split()))
        N.insert(0, 0)
        distancias = []
        for i in range(1, len(N)):
            distancia = N[i] - N[i - 1]
            distancias.append(distancia)

        distancias.sort(reverse=True)

        total = sum(distancias[K-1:])
        print(total)
    except EOFError:
        break
