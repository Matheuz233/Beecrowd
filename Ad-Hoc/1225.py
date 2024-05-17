while True:
    try:
        n = int(input())
        N = list(map(int, input().split()))
        soma_N = sum(N)

        if all(numero == N[0] for numero in N):
            print(1)
        else:
            media = soma_N // n
            if soma_N % n != 0:
                print(-1)
            else:
                soma_N = soma_N//n
                alto = 0
                for i in range(n):
                    if N[i] > soma_N:
                        alto += N[i] - soma_N
                print(alto + 1)
    except EOFError:
        break
