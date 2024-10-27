n, x = map(int, input().split())
viewpoints = list(map(int, input().split()))

anterior = False
total = 0

resultados = []

for i in range(1, len(viewpoints)):
    if viewpoints[i] - viewpoints[i-1] <= x:
      total += 1
      anterior = True
    elif anterior:
      anterior = False
      resultados.append(total)
      total = 0

resultados.append(total)

resultados.sort(reverse=True)

print(resultados[0] + 1)
