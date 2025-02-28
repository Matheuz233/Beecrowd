for _ in range(int(input())):
    entrada=list(map(int,input().split()))
    k=entrada.pop(0)
    print(sum(entrada) - k+1)