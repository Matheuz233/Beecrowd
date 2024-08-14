entrada = input()
caso = 1

while entrada != "*":

    entrada_duplicada = entrada + entrada

    resultados = []

    index_final = len(entrada) + 1

    for i in range(1, len(entrada_duplicada) - len(entrada) + 1):
        resultados.append(entrada_duplicada[i:index_final])
        index_final += 1

    print(f"Caso {caso}: {min(resultados)} {max(resultados)}")

    entrada = input()
    caso += 1
