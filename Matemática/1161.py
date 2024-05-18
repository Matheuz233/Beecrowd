def fazerFatorial(num):
    total = 1
    for i in range(1, num+1):
        total *= i
    return total
while True:
    try:
        M, N = map(int, input().split())
        resultado = fazerFatorial(M) + fazerFatorial(N)
        print(resultado)
    except EOFError:
        break