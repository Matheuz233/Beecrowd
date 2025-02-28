porcoes = [300, 1500, 600, 1000, 150]

resultado = 225

for i in range(5):
    entrada = int(input())
    resultado += entrada * porcoes[i]

print(resultado)
