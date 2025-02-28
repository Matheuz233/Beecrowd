for i in range(1, int(input()) + 1):
    entrada = list(map(int, input().split()))

    n = entrada.pop(0)

    print(f"Case {i}: {entrada[(n//2)]}")  