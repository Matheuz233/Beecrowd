while True:
    n, m = map(int, input().split())

    t = list(map(int, input().split()))

    if n == 0 and m == 0:
        break
    
    unicos = []
    repetidos = []

    for i in t:
        if unicos.count(i) == 0:
            unicos.append(i)
        else:
            if repetidos.count(i) == 0:
                repetidos.append(i)
    
    print(len(repetidos))
