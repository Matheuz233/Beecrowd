for _ in range(int(input())):
    c = float(input())
    total = 0
    while c > 1:
        c /= 2
        total += 1
    print(f"{total} dias")
