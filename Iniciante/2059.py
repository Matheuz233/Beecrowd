p, j1, j2, r, a = map(int, input().split())

ganhador = 0

if p == 1:
    if (j1 + j2) % 2 == 0:
        ganhador = 1
    else: 
        ganhador = 2
else: 
    if (j1 + j2) % 2 == 0:
        ganhador = 2
    else:
        ganhador = 1

if r == 1:
    if a == 1:
        ganhador = 2
    else:
        ganhador = 1

print(f"Jogador {ganhador} ganha!")