risada = input()

vogais = []

for i in risada:
    if i in ["a", "e", "i", "o", "u"]:
        vogais.append(i)

reverso_vogais = vogais[::-1]

iguais = True

for i in range(len(vogais)):
    if vogais[i] != reverso_vogais[i]:
        iguais = False
        break

if iguais:
    print("S")
else:
    print("N")