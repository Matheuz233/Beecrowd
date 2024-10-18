for _ in range(int(input())):
    lista = sorted(list(map(str, input().split())))

    for i in lista:
        if lista.count(i) > 1:
            while lista.count(i) != 1:
                lista.remove(i)

    print(" ".join(lista))
