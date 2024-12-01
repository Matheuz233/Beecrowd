N = int(input())

hobbits = 0
humanos = 0
elfos = 0
anoes = 0
magos = 0

for _ in range(N):
    nome, raca = input().split()

    if raca == 'X':
        hobbits += 1
    elif raca == 'H':
        humanos += 1
    elif raca == 'E':
        elfos += 1
    elif raca == 'A':
        anoes += 1
    elif raca == 'M':
        magos += 1

print(f"{hobbits} Hobbit(s)")
print(f"{humanos} Humano(s)")
print(f"{elfos} Elfo(s)")
print(f"{anoes} Anao(oes)")
print(f"{magos} Mago(s)")
