for _ in range(int(input())):
    palavras = list(map(str, input().split()))

    palavras_ordenadas = sorted(palavras, key=len, reverse=True)

    print(" ".join(palavras_ordenadas))
