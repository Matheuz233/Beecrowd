for _ in range(int(input())):
    n, m = map(int, input().split(" "))
    resultado = list(str(n**m))
    print(len(resultado))
