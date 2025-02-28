for i in range(1, int(input())+1):
    n, k = map(int, input().split(" "))
    resultado = 0

    for j in range(1, n + 1):
        resultado = (resultado + k) % j

    print(f"Case {i}: {resultado + 1}")
