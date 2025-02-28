N = int(input())

P = list(map(int, input().split()))

P.sort()

meio = int(len(P)/2)

if len(P) % 2 == 0:
    print(int((P[meio-1] + P[meio])/2))
else:
    print(P[meio])
