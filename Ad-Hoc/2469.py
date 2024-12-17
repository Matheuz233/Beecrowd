n = int(input())
notas = list(map(int, input().split()))

notas.sort(reverse=True)

frequencia = 0
valor = 0

for i in notas:
    if notas.count(i) > frequencia:
        frequencia = notas.count(i)
        valor = i

print(valor)