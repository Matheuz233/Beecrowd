n = int(input())
medidas = list(map(int, input().split()))
resposta = 0

for i in range(1,n):
  if medidas[i] < medidas[i - 1]:
    resposta = i + 1
    break

print(resposta)
