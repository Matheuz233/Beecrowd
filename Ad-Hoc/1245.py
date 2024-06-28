while True:
    try:
        direito = {}
        esquerdo = {}

        for _ in range(int(input())):
            M, L = input().split()
            if L == "D":
                if M in direito:
                    direito[M] += 1
                else:
                    direito[M] = 1
            else:
                if M in esquerdo:
                    esquerdo[M] += 1
                else:
                    esquerdo[M] = 1

        total = 0

        for tamanho, count in direito.items():
            if tamanho in esquerdo:
                total += min(count, esquerdo[tamanho])

        print(total)

    except EOFError:
        break
