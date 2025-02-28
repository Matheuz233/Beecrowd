def entregas(tempos, pizzas, p, idx):
    if idx == len(tempos):
        return 0

    tempo_excluido = entregas(tempos, pizzas, p, idx + 1)

    if pizzas[idx] <= p:
        tempo_incluido = tempos[idx] + \
            entregas(tempos, pizzas, p - pizzas[idx], idx + 1)
        return max(tempo_excluido, tempo_incluido)

    return tempo_excluido


while True:
    n = int(input())
    if n == 0:
        break

    p = int(input())
    tempos = []
    pizzas = []

    for _ in range(n):
        tempo, pizza = map(int, input().split())
        tempos.append(tempo)
        pizzas.append(pizza)

    resultado = entregas(tempos, pizzas, p, 0)
    print(f"{resultado} min.")
