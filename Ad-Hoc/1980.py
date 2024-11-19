s = input().strip()

while s != "0":
    resultado = 1
    for i in range(1, len(s) + 1):
        resultado *= i

    print(resultado)

    s = input().strip()
