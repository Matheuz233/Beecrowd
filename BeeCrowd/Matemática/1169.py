for _ in range(int(input())):
    x = int(input())

    index = 1
    resultados = [1]
    total = 0

    while index != x:
        resultados.append(resultados[index-1]*2)

        index += 1

    print(f"{(sum(resultados)//12)//1000} kg")
