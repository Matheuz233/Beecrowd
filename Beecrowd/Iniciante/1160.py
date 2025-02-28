for _ in range(int(input())):
    PA, PB, G1, G2 = map(float, input().split(" "))
    contador = 0
    PA = int(PA)
    PB = int(PB)

    while PA <= PB:
        PA = PA + int((G1*PA/100))
        PB = PB + int((G2*PB/100))
        contador += 1
        if contador > 100:
            break
    if contador > 100:
        print(f"Mais de 1 seculo.")
    else:
        print(f"{contador} anos.")
