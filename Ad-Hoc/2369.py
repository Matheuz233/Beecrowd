consumo = int(input())
valorTotal = 7
if consumo > 10:
    if consumo > 30:
        valorTotal += 20
    else:
        valorTotal += (consumo - 10) * 1
    if consumo > 100:
        valorTotal += 70 * 2
    elif consumo > 30:
        valorTotal += (consumo - 30) * 2
    if consumo > 100:
        valorTotal += (consumo - 100) * 5
print(valorTotal)
