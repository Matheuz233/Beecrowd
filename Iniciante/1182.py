coluna = int(input())
operacao = input()

array = []

for i in range(12):
    for j in range(12):
        entrada = float(input())

        if j == coluna:
            array.append(entrada)

if operacao == "S":
    print(f"{sum(array):.1f}")
else:
    print(f"{sum(array)/12:.1f}")