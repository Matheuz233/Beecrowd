comidas = {
    "suco": 120,
    "morango": 85,
    "mamao": 85,
    "goiaba": 70,
    "manga": 56,
    "laranja": 50,
    "brocolis": 34
}

entrada = int(input())

while entrada != 0:
    total = 0
    for _ in range(entrada):
        entrada = list(map(str, input().split(" ")))

        quantidade, comida = int(entrada[0]), entrada[1]

        total += (comidas[comida] * quantidade)

    if total >= 110 and total <= 130:
        print(f"{total} mg")
    if total > 130:
        print(f"Menos {total - 130} mg")
    if total < 110:
        print(f"Mais {110 - total} mg")

    entrada = int(input())
