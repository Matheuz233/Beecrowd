for _ in range(int(input())):
    b = int(input())
    a1, d1, l1 = map(int, input().split())
    a2, d2, l2 = map(int, input().split())

    valorGolpeDabriel = (a1 + d1)/2
    valorGolpeGuarte = (a2 + d2)/2

    if l1 % 2 == 0:
        valorGolpeDabriel += b
    if l2 % 2 == 0:
        valorGolpeGuarte += b
    
    if valorGolpeDabriel == valorGolpeGuarte:
        print("Empate")
    elif valorGolpeDabriel > valorGolpeGuarte:
        print("Dabriel")
    else:
        print("Guarte")