while True:
    b, n = map(int, input().split())
    if b == 0 and n == 0:
        break

    reservas = list(map(int, input().split()))

    for _ in range(n):
        d, c,v = map(int, input().split())
        reservas[d - 1] -= v
        reservas[c - 1] += v

    positivo = True
    for reserva in reservas:
        if reserva < 0:
            positivo = False
            break

    if positivo:
        print("S")
    else:
        print("N")
