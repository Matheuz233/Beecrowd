for _ in range(int(input())):
    X, Y = map(int, input().split())

    impares = []

    index = X

    while len(impares) != Y:
        if index % 2 != 0:
            impares.append(index)
        index += 1
        
    print(sum(impares))