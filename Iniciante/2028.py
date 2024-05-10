contador = 1
while True:
    try:
        n = int(input())
        lista_num = [0,]
        for x in range(1, n+1):
            for y in range(x):
                lista_num.append(x)
        if len(lista_num) == 1:
            print(f"Caso {contador}: {len(lista_num)} numero")
            print(" ".join(map(str, lista_num)))
            print()
        else:
            print(f"Caso {contador}: {len(lista_num)} numeros")
            print(" ".join(map(str, lista_num)))
            print()
        contador += 1

    except EOFError:
        break