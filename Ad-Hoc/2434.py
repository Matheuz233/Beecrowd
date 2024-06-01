N, S  = map(int, input().split(" "))
Saldos = []
T = S
for _ in range(N):
    V = int(input())
    T += V
    Saldos.append(T)
Saldos.sort()
print(Saldos[0])