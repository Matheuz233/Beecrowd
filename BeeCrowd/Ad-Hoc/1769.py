import sys

cpfs = sys.stdin.read().strip().splitlines()

for cpf in cpfs:
    partes = cpf.split("-")
    primeiraParte = partes[0].replace(".", '')
    segundaParte = partes[1]

    b1, b2 = [], []

    for i in range(9):
        b1.append(int(primeiraParte[i]) * (i + 1))

    digito1 = sum(b1) % 11
    if digito1 == 10:
        digito1 = 0

    for i in range(9):
        b2.append(int(primeiraParte[i]) * (9 - i))

    digito2 = sum(b2) % 11
    if digito2 == 10:
        digito2 = 0

    if digito1 == int(segundaParte[0]) and digito2 == int(segundaParte[1]):
        print("CPF valido")
    else:
        print("CPF invalido")
