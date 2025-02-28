caso = 0

while True:
    caso += 1

    try:
        n = str(input())
        numeros = list(input().split())

        resultado = []
        total = 0

        while numeros.count(n) != 0:
            tamanho = numeros[numeros.index(n)]
            sexo = numeros[numeros.index(n) + 1]

            resultado.append(tamanho)
            resultado.append(sexo)

            numeros.remove(tamanho)
            numeros.remove(sexo)

            total += 1
        
        feminino = resultado.count("F")
        masculino = resultado.count("M")

        if caso > 1:
            print()
        
        print(f"Caso {caso}:")
        print(f"Pares Iguais: {total}")
        print(f"F: {feminino}")
        print(f"M: {masculino}")

    except EOFError:
        break