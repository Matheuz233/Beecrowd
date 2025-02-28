while True:
    try:
        numPalavra, numMaxLinha, caractereLinha = map(int, input().split(" "))
        N = list(input().split(" "))
        total = 0
        linha = 0
        for x in N:
            total += 1
            if len(x) + total <= caractereLinha:
                total += len(x) 
            else:
                total -= 1

            if len(x) + total <= caractereLinha:
                linha += 1
                total = len(x) 
        if total > 0:
            linha += 1

        pagina = 0
        while linha > 0:
            linha -= numMaxLinha
            pagina +=1

        print(pagina)
        
    except EOFError:
        break
