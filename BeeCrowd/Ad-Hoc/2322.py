n = int(input())

entradas = list(map(int, input().split()))

for i in range(1, n+1):
    if entradas.count(i) == 0:
        print(i)
