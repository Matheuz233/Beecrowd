n = int(input())
letras = list(map(str, input().split()))

letras = sorted(letras)

posicoes = []

limite  = (ord(letras[0]) - 65) + n

total = 0

for letra in letras:
    posicao = (ord(letra) - 65)
    if posicao > limite:
        total += 1

print(total)