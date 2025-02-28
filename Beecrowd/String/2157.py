for _ in range(int(input())):
    b, e = map(int, input().split())

    sequencia, reverso = [], []

    for i in range(b,e+1):
        sequencia.append(i)

    for j in sequencia:
        j = str(j)
        j = j[::-1]
        reverso.append(j)

    resultado = sequencia + reverso[::-1]

    print(''.join(map(str,resultado)))