for _ in range(int(input())):
    a, b = map(str, input().split())

    total = len(a) - len(b)
    if int(a[total:]) == int(b):
        print("encaixa")
    else:
        print("nao encaixa")