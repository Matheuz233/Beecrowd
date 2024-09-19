notas = []

for _ in range(int(input())):
  matricula, nota = map(float, input().split())
  notas.append([matricula, nota])

notas.sort(key=lambda x: x[1])

maior = notas[-1][1]

if maior >= 8.0:
  print(int(notas[-1][0]))
else:
  print("Minimum note not reached")