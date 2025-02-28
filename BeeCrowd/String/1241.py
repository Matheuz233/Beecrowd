for _ in range(int(input())):
    a, b = map(str, input().split())
    diferença = len(a) - len(b)

    if a[diferença:] == b:
        print("encaixa")
    else:
        print("nao encaixa")
