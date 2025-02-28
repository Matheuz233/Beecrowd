N, M = map(int, input().split(" "))
i = 0
resultado = 0
gols = []
jogador = [0 for _ in range(N)]

while i <= N-1:
    gols.append(list(map(int, input().split(" "))))
    i += 1

for x in range(0, N):
    for y in range(0, M):
        if (gols[x][y] > 0):
            jogador[x] += 1


for i in range(N):
    if(jogador[i] == M):
        resultado += 1

print(resultado)