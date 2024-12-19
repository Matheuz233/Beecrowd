while True:
    try:
        n, min, max = map(int, input().split())

        total = 0

        for _ in range(n):
            a = int(input())

            if a <= max and a >= min:
                total += 1

        print(total)
        
    except EOFError:
        break