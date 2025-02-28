for _ in range(int(input())):
    j1, escolha1, j2, escolha2 = map(str, input().split())
    n1, n2 = map(int, input().split())

    if (n1 + n2) % 2 == 0:
        if escolha1 == "PAR":
            print(j1)
        else:
            print(j2)
    else:
        if escolha1 == "IMPAR":
            print(j1)
        else:
            print(j2)
