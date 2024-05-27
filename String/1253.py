alfabeto = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]

for _ in range(int(input())):
    caracteres = list(input())
    deslocar = int(input())

    resultado = []

    for i in caracteres:
        nova_letra = alfabeto.index(i) - deslocar
        resultado.append(alfabeto[nova_letra])
    
    print(''.join(resultado ))
