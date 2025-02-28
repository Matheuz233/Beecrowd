from math import ceil

v, n = map(int, input().split())

placasTotais = v * n

placaPercurso = []

for i in range(10, 100, 10):
    placaPercurso.append(ceil((placasTotais * i)/100))
print(" ".join(str(x) for x in placaPercurso))
