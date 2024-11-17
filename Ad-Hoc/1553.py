n, k = map(int, input().split())

while n != 0 and k != 0:
    ps = list(map(int, input().split()))

    total = 0

    counts = {}
    for p in ps:
        counts[p] = counts.get(p, 0) + 1

    for v in counts.values():
        if v >= k:
            total += 1

    print(total)
    n, k = map(int, input().split())
