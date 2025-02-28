casos = 1

while True:
    try:
        n = list(input())
        sequencia = list(input())

        index, total, posicao = 0, 0, 0

        for i in range(len(sequencia)):
            if sequencia[i] == n[index]:
                index += 1
                if index == len(n):
                    total += 1
                    posicao = i
                    index = 0
            else:
                if sequencia[i] == n[0]:
                    index = 1
                else:
                    index = 0

        print(f"Caso #{casos}:")
        if total > 0:
            print(f"Qtd.Subsequencias: {total}")
            print(f"Pos: {posicao - len(n) + 2}")
        else:
            print("Nao existe subsequencia")
        print()

        casos += 1

    except EOFError:
        break
