for _ in range(int(input())):
    x, y = map(int, input().split())

    rafael = (3*x)**2 + y**2
    beto = 2*(x**2) + (5*y)**2
    carlos = -100*x + y**3

    if rafael > beto and rafael > carlos:
        print("Rafael ganhou")
    if beto > rafael and beto > carlos:
        print("Beto ganhou")
    if carlos > beto and carlos > rafael:
        print("Carlos ganhou")
