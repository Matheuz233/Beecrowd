n, m = map(int, input().split())

campo = []

for i in range(n):
    entrada = list(map(int, input().split()))
    campo.append(entrada)

print(campo)

for i in range(m):
  for j in range(n):
    print(i, j)