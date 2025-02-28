while True:
    try:
        h, m = map(int, input().split())

        totalHoras = 0

        while h > 0:
            h -= 30
            totalHoras += 1

        totalMinutos = 0

        while m > 0:
            m -= 6
            totalMinutos += 1
        totalHoras = str(totalHoras)
        totalMinutos = str(totalMinutos)
        print(f"{totalHoras.zfill(2)}:{totalMinutos.zfill(2)}")
    except EOFError:
        break
