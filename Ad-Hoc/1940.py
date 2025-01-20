j, r = map(int, input().split())

pontos = list(map(int, input().split()))

resultado = [0] * j

for i in range(0, len(pontos), j):
  rodada = pontos[i:j+i]
  for k in range(j):
    resultado[k] += rodada[k]

maiorValor = max(resultado)

ultimoIndex = -1
for i in range(len(resultado)):
    if resultado[i] == maiorValor:
        ultimoIndex = i

print(ultimoIndex + 1)