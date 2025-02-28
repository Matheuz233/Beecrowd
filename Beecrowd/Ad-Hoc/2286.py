total = 1

while True:
    try:
        n = int(input())

        if n == 0:
            break

        j1 = input()
        j2 = input()

        print(f"Teste {total}")

        for _ in range(n):
            n1, n2 = map(int, input().split())
            total_partida = n1 + n2
            if total_partida % 2 == 0:
                print(j1)
            else:
                print(j2)

        total += 1

        print()

    except EOFError:
        break
