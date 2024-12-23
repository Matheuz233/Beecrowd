mensagem = input()
decodificada = ""
pular = False

for letra in mensagem:
    if pular:
        decodificada += letra
        pular = False
    elif letra == 'p':
        pular = True
    else:
        decodificada += letra

print(decodificada)
