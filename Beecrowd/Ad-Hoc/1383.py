for caso in range(1, int(input()) + 1):
    matriz = []
    for _ in range(9):
        linha = list(map(int, input().split()))
        matriz.append(linha)

    parada = False

    for i in range(9):
        casos_linha = []
        casos_coluna = []
        for j in range(9):
            if matriz[i][j] in casos_linha:
                parada = True
                break
            casos_linha.append(matriz[i][j])

            if matriz[j][i] in casos_coluna:
                parada = True
                break
            casos_coluna.append(matriz[j][i])
        if parada:
            break

    if not parada:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                bloco = []
                for k in range(3):
                    for l in range(3):
                        if matriz[i + k][j + l] in bloco:
                            parada = True
                            break
                        bloco.append(matriz[i + k][j + l])
                    if parada:
                        break
                if parada:
                    break
            if parada:
                break

    print(f"Instancia {caso}")
    if parada:
        print("NAO")
    else:
        print("SIM")
    print("")
