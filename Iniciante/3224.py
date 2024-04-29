def contar_ocorrencias(caractere, lista):
    return lista.count(caractere)

g1 = list(input())
g2 = list(input())

a = contar_ocorrencias('a', g1)
b = contar_ocorrencias('a', g2)

if a >= b:
    print("go")
if a < b:
    print("no")
