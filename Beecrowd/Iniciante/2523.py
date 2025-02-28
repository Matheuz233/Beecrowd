while True:
    try:
        string = input()
        n = int(input())
        l = list(map(int, input().split()))

        resultado = []

        for i in l:
            resultado.append(string[i-1])
        
        print("".join(resultado))
    except EOFError:
        break