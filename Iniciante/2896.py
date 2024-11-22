for _ in range(int(input())):
    n, k = map(int, input().split())
    total = int(int(n % k) + int(n / k))
    print(total)