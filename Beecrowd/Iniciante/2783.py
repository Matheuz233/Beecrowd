figurinhas, figurinhasCarimbadas, figurinhasCompradas = map(int, input().split())
carimbadas = list(map(int, input().split()))
compradas = list(map(int, input().split()))

total = 0

for i in carimbadas:
    if i in compradas:
        total += 1

print(len(carimbadas) - total)
