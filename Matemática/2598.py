for _ in range(int(input())):
    n, m = map(int, input().split())

    total = n//m

    if n % m != 0:
        total += 1

    print(total)
