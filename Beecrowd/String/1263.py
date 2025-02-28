while True:
    try:
        entrada = list(map(str, input().split()))
        atual = ""
        sequencia, total = 0, 0
        for i in range(len(entrada)):
            if entrada[i][0].lower() == atual:
                sequencia += 1
            elif entrada[i][0].lower() != atual and sequencia >= 1:
                total += 1
                sequencia = 0
            atual = entrada[i][0].lower()

        if sequencia >= 1:
            print(total + 1)
        else:
            print(total)

    except EOFError:
        break
