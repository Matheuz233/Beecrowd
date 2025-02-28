e, f, c = map(int, input().split())
garrafas = e + f
total = 0

while garrafas >= c:
    novos = garrafas // c
    total += novos
    garrafas = garrafas % c + novos

print(total)
