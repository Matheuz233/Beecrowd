N = int(input())

carrinhos = 0
bonecas = 0

for _ in range(N):
    nome, genero = input().split()

    if genero == 'M':
        carrinhos += 1
    elif genero == 'F':
        bonecas += 1

print(f"{carrinhos} carrinhos")
print(f"{bonecas} bonecas")
