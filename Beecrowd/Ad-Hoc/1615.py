for _ in range(int(input())):
    n, m = map(int, input().split())
    votos = list(map(int, input().split()))

    resultado = []

    for i in range(1, n+1):
        resultado.append(votos.count(i))

    if resultado[resultado.index(max(resultado))] > m // 2:
        print(resultado.index(max(resultado))+1)
    else:
        print(-1)