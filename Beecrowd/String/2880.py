def comparar_strings(string1, string2):
    for i in range(len(string1)):
        if string1[i] == string2[i]:
            return False
    return True

cifrada = input()
crib = input()

index_inicial = 0
index_final = len(crib)

total = 0

while index_final <= len(cifrada):
    cifrada_cortada = cifrada[index_inicial:index_final]

    bol_comparacao = comparar_strings(cifrada_cortada, crib)
    if bol_comparacao:
        total += 1

    index_inicial += 1
    index_final += 1

print(total)
