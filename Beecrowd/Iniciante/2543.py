while True:
    try:
        n, c = map(int, input().split())
        total = 0

        for _ in range(n):
            i, j = map(int, input().split())

            if c == i and j == 0:
                total += 1

        print(total)

    except EOFError:
        break
